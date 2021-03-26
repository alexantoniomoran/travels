import random

from braces.views import CsrfExemptMixin
from constance import config
from django.conf import settings
from django.views.generic import TemplateView

from website.api.constants import PHOTO_TYPES
from website.api.models import Photo
from website.api.serializers import PhotoSerializer


class MainPageView(CsrfExemptMixin, TemplateView):
    template_name = "bootstrap_main_page.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["GOOGLE_MAP_HEIGHT"] = config.GOOGLE_MAP_HEIGHT
        context["GOOGLE_MAP_URL"] = config.GOOGLE_MAP_URL
        context["GOOGLE_MAP_WIDTH"] = config.GOOGLE_MAP_WIDTH
        return context


class PhotosView(CsrfExemptMixin, TemplateView):
    template_name = "photos.html"

    def get_random_photos(self, qs):
        possible_ids = list(qs.values_list("id", flat=True))
        possible_ids = random.sample(possible_ids, k=int(config.DISPLAY_NUMBER))
        return qs.filter(pk__in=possible_ids)

    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        context["debug"] = settings.DEBUG
        context["filters"] = PHOTO_TYPES.values

        photos = Photo.objects.all()
        random_photos = self.get_random_photos(photos)
        serializer = PhotoSerializer(instance=random_photos, many=True)
        context["photos"] = serializer.data

        return context
