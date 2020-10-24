from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("about", views.about, name="about"),
               path("features", views.features, name="features"),
               path("writing", views.writing, name="writing")]
