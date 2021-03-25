from django.conf.urls import url

from website.api.views import PhotosView

urlpatterns = [
    url("photos", PhotosView.as_view(), name="photos-page"),
]
