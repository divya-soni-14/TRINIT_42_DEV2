from django.shortcuts import redirect, render

from .models import *  # table DATA   field1(string) | field2(int)


def home(request):
 
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
