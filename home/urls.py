from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("home", views.home, name="home"),
               path("info_user", views.infouser, name="info_user"),
               path("surroundings", views.surroundings, name="surroundings"),
               path("my_profile", views.my_profile, name="my_profile"),
               path("know_you", views.know_you, name="know_you"),
               path("contact_us", views.contact_us, name="contact_us"),
               path("settings", views.settings, name="settings"),
               path("add_resource", views.add_resource, name="add_resource"),
               path("help", views.help, name="help"),
               path("surroundings_shape_level0_identify", views.surroundings_shape_level0_identify, name="surroundings_shape_level0_identify"),
               path("writing", views.writing, name="writing")]
