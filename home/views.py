from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def writing(request):
    return render(request, 'writing.html')

def infouser(request):
    return render(request,'info_user.html')

def surroundings(request):
    return render(request,'know_your_surroundings.html')

def know_you(request):
    return render(request,'know_you.html')
