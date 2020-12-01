from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def writing_level0(request):
    return render(request, 'writing_level0.html')

def writing_level1(request):
    return render(request, 'writing_level1.html')


def writing_level2(request):
    return render(request, 'writing_level2.html')


def add_image_know_you(request):
    return render(request, 'add_image_know_you.html')


def know_you_level1(request):
    return render(request, 'know_you_level1.html')


def infouser(request):
    return render(request,'info_user.html')


def surroundings(request):
    return render(request,'know_your_surroundings.html')


def know_you(request):
    return render(request,'know_you.html')


def my_profile(request):
    return render(request,'my_profile.html')


def contact_us(request):
    return render(request,'contact_us.html')


def settings(request):
    return render(request,'settings.html')


def add_resource(request):
    return render(request,'add_resource.html')

def help(request):
    return render(request,'help.html')

def surroundings_shape_level0_identify(request):
    return render(request,'surroundings_shape_level0_identify.html')

def shape_level1_learn(requset):
    return render(requset,'shape_level1_learn.html')

def object_level0_learn(request):
    return render(request,'object_level0_learn.html')

def english_number_level0(request):
    return render(request, 'english_number_level0.html')

def bangla_charecter_level0(request):
    return render(request, 'bangla_charecter_level0.html')

def bangla_number_level0(request):
    return render(request, 'bangla_number_level0.html')

def anime(request):
    return render(request, 'anime.html')