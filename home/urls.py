from django.urls import path

from upload_image.views import image_view
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("home", views.home, name="home"),
               path("info_user", views.infouser, name="info_user"),
               path("surroundings", views.surroundings, name="surroundings"),
               path("my_profile", views.my_profile, name="my_profile"),
                path("know_you", views.know_you, name="know_you"),
               path("contact_us", views.contact_us, name="contact_us"),
               path("settings", views.settings, name="settings"),
               path("image_upload", image_view, name="add_resource"),
               path("help", views.help, name="help"),
               path("surroundings_shape_level0_identify", views.surroundings_shape_level0_identify,
                    name="surroundings_shape_level0_identify"),
               path("shape_level1_learn", views.shape_level1_learn, name="shape_level1_learn"),
               path("object_level0_learn", views.object_level0_learn, name="object_level0_learn"),
               path("english_number", views.english_number_level0, name="english_number"),
               path("bangla_charecter", views.bangla_charecter_level0, name="bangla_charecter"),
               path("bangla_number", views.bangla_number_level0, name="bangla_number"),
               path("writing_level1", views.writing_level1, name="writing_level1"),
               path("writing_level2", views.writing_level2, name="writing_level2"),
               path("add_image_know_you", views.add_image, name="add_image_know_you"),
               path("know_you_level1", views.know_you_level1, name="know_you_level1"),
               path('success', views.success, name='success'),
               path("anime", views.anime, name="anime"),
               path("writing", views.writing_level0, name="writing"),
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
