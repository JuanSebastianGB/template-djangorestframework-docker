from django.urls import path

from . import views


urlpatterns = [
    path("users", views.UserListCreate.as_view(), name="create-user-list"),
    path(
        "user/<int:pk>/",
        views.UserRetrieveUpdateDelete.as_view(),
        name="user-Details",
    ),
]
