from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("home", views.home, name="home"),
               path("info_user", views.infouser, name="info_user"),
               path("writing", views.writing, name="writing")]
