from django.urls import include, path


from .views import AlbumViewSet, TrackViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"albums", AlbumViewSet, basename="album")
router.register(r"tracks", TrackViewSet, basename="track")

urlpatterns = [
    path("", include(router.urls)),
]
