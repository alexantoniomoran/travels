from django.contrib import admin

from website.api.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ("photo", "photo_type", "title", "description")
    list_display = ("thumbnail_image", "photo_type", "title", "description")
    readonly_fields = ("thumbnail_image",)
