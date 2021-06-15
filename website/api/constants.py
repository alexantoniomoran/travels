from django.db import models


class PHOTO_TYPES(models.TextChoices):
    CRAFT = "craft", "Crafts"
    PANORAMA = "panorama", "Panoramas"
    RECIPE = "recipe", "Recipes"
    WILDLIFE = "wildlife", "Wildlife"
