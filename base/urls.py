from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<int:id>/", views.room, name="room"),
    path("create/", views.createRoom, name="create"),
    path("edit/<int:id>/", views.editRoom, name="edit"),
]
