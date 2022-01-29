from django.shortcuts import redirect, render
from .models import *  # table DATA   field1(string) | field2(int)


def home(request):
    allUsers = users.objects.all()
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def register_teamcode(request):
    return render(request, 'register_teamcode.html')

def dashboard(request):
    return render(request, 'dashboard.html')