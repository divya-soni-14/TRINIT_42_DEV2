
from django.contrib.auth.hashers import make_password

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from .models import *

#table users, bugs, messages , teams, softwares

def register(request):
    response = {}
    if request.method == 'POST':
        user = users()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.password = make_password(request.POST.get('password'))
        user.firstname = request.POST.get('firstname')
        user.lastname = request.POST.get('lastname')
        user.company = request.POST.get('company')
        user.organisation = request.POST.get('organisation')
        user.save()
    else:
        return render(request, "login.html")

def lin(request):
    if request.user.is_authenticated:
        print("alledyy man")
        return redirect('home')
    if request.method == 'POST':
            response = {}
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            password = make_password(password,salt="nothing")
            user = users.objects.get(username=username)
            print(password,user.password)
            if user.password == password:
                print(user._meta)
                login(request, user)
                print("success")
                return redirect('home')
            else:
                response['error'] = 'username and password do not match.'
                print("offo")
                return render(request, 'login.html', response)
    else:
        print("bypasss")
        return render(request, 'login.html')

def lout(request):
    logout(request)
    return home(request)



def home(request):
    response = {}
    # users.objects.create(username = "kiwi", password = make_password("kiwi",salt="nothing"), email="kiwi@google.com", firstname = "kiwi", lastname = "kiwi", organisation = "kiwi")
    # response['data'] = request.user
    return render(request,'home.html',response)





def register(request):
    return render(request, "register.html")
