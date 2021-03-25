from braces.views import CsrfExemptMixin
from constance import config
from django.views.generic import TemplateView

from website.api.constants import PHOTO_TYPES
from website.api.models import Photo
from website.api.serializers import PhotoSerializer


class MainPageView(CsrfExemptMixin, TemplateView):
    template_name = "bootstrap_main_page.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["GOOGLE_MAP_URL"] = config.GOOGLE_MAP_URL
        return context


class PhotosView(CsrfExemptMixin, TemplateView):
    template_name = "photos.html"

    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        context["filters"] = PHOTO_TYPES.values

        photos = Photo.objects.all()
        serializer = PhotoSerializer(instance=photos, many=True)
        context["photos"] = serializer.data
        return context
