from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/<int:id>/", views.room, name="room"),
    path("submit/", views.submitRoom, name="submit"),
    path("edit/<int:id>/", views.editRoom, name="edit"),
    path("delete/<int:id>/", views.deleteRoom, name="delete"),
]
