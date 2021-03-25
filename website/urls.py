from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from website.api.views import MainPageView, PhotosView


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path("__admin__/", admin.site.urls),
    path("api/", include("website.api.urls")),
    url("^$", MainPageView.as_view(), name="main-page",),
]
