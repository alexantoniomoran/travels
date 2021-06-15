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
        context["GOOGLE_MAP_URL"] = config.GOOGLE_MAP_URL
        return context


class PhotosView(CsrfExemptMixin, TemplateView):
    template_name = "photos.html"

    @staticmethod
    def get_random_photos(cleaned_filters, qs):
        return_list = []
        for photo_type in cleaned_filters:
            type_ids = list(
                qs.filter(photo_type=photo_type).values_list("id", flat=True)
            )
            if not type_ids:
                continue

            sample_type_ids = random.sample(type_ids, k=1)
            return_list.append(qs.filter(pk__in=sample_type_ids).first())

        possible_ids = list(
            qs.exclude(id__in=[i.id for i in return_list]).values_list("id", flat=True)
        )
        number_to_sample = min(
            (int(config.DISPLAY_NUMBER) - len(return_list)), len(possible_ids)
        )
        sample_possible_ids = random.sample(possible_ids, k=number_to_sample)
        return_list.extend(list(qs.filter(pk__in=sample_possible_ids)))

        return return_list

    @staticmethod
    def get_filters_with_exclusions():
        exclude_filters = [i.strip().lower() for i in config.EXCLUDE_FILTER.split(",")]
        return [i for i in PHOTO_TYPES.values if i not in exclude_filters]

    def get_context_data(self, **kwargs):
        cleaned_filters = self.get_filters_with_exclusions()

        context = super(PhotosView, self).get_context_data(**kwargs)
        context["debug"] = settings.DEBUG
        context["filters"] = cleaned_filters

        photos = Photo.objects.filter(photo_type__in=cleaned_filters)
        random_photos = self.get_random_photos(cleaned_filters, photos)
        serializer = PhotoSerializer(instance=random_photos, many=True)
        context["photos"] = serializer.data

        return context
