from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def writing(request):
    return render(request, 'writing.html')


def infouser(request):
    return render(request, 'info_user.html')


def surroundings(request):
    return render(request, 'know_your_surroundings.html')


def know_you(request):
    return render(request, 'know_you.html')


def my_profile(request):
    return render(request, 'my_profile.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def settings(request):
    return render(request, 'settings.html')


def add_resource(request):
    return render(request, 'add_resource.html')


def help(request):
    return render(request, 'help.html')


def surroundings_shape_level0_identify(request):
    return render(request, 'surroundings_shape_level0_identify.html')


def shape_level1_learn(requset):
    return render(requset, 'shape_level1_learn.html')


def object_level0_learn(request):
    return render(request, 'object_level0_learn.html')
