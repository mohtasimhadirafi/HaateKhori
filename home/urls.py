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
               path("shape_level1_learn", views.shape_level1_learn, name="shape_level1_learn"),
               path("object_level0_learn", views.object_level0_learn, name="object_level0_learn"),
               path("english_number", views.english_number_level0, name="english_number"),
               path("bangla_charecter", views.bangla_charecter_level0, name="bangla_charecter"),
               path("bangla_number", views.bangla_number_level0, name="bangla_number"),
               path("writing", views.writing, name="writing")]
