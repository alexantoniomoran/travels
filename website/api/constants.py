from django.db import models


class PHOTO_TYPES(models.TextChoices):
    PANORAMA = "panorama", "Panorama"
    RECIPE = "recipe", "Recipe"
    WILDLIFE = "wildlife", "Wildlife"
