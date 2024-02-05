from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, StudentViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="student")
router.register(r"modules", ModuleViewSet, basename="module")


urlpatterns = [
    path("", include(router.urls)),
]
