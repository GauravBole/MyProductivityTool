from django.shortcuts import render

# Create your views here.


def projects(request):
    return render(request, 'project/projects.html')


def login(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')