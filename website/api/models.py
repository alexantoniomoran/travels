import cloudinary.uploader
import os
import sys

from constance import config
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.safestring import mark_safe
from io import BytesIO
from PIL import Image

from website.api.constants import PHOTO_TYPES


class Photo(models.Model):
    photo = models.ImageField(upload_to="images/")
    photo_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=PHOTO_TYPES.choices,
        help_text="The 'type' of photo being uploaded",
    )
    title = models.CharField(max_length=512, null=True, blank=True, default="")
    description = models.CharField(max_length=512, null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def thumbnail_image(self):
        return mark_safe(
            f'<img src="{self.photo.url}" height={config.THUMBNAIL_HEIGHT} width={config.THUMBNAIL_WIDTH} />'
        )

    def delete(self, *args, **kwargs):
        if settings.DEBUG:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.name))
        else:
            cloudinary.uploader.destroy(self.photo.name, invalidate=True)

        super(Photo, self).delete(*args, **kwargs)

    def _compress_image(self, photo):
        image_extension = photo.name.split(".")[1]
        image_type = "PNG" if image_extension.lower() == "png" else "JPEG"

        output_stream = BytesIO()
        temp_image = Image.open(photo)
        temp_image.save(output_stream, format=image_type, quality=20, optimize=True)
        output_stream.seek(0)

        return InMemoryUploadedFile(
            output_stream,
            "ImageField",
            photo.name,
            f"image/{image_type.lower()}",
            sys.getsizeof(output_stream),
            None,
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.photo = self._compress_image(self.photo)

        super(Photo, self).save(*args, **kwargs)
