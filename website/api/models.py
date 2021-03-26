import os
import cloudinary.uploader

from constance import config
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe

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
