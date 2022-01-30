from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    UpdateView,
)

from .forms import *
from .models import *

# table users, bugs, messages , teams, softwares


def register(request):
    response = {}
    # if request.method == 'POST':
    # user = users()
    # user.username = request.POST.get('username')
    # user.email = request.POST.get('email')
    # user.password = make_password(request.POST.get('password'))
    # user.firstname = request.POST.get('firstname')
    # user.lastname = request.POST.get('lastname')
    # user.company = request.POST.get('company')
    # user.organisation = request.POST.get('organisation')
    # user.save()
    # else:
    return render(request, "register.html")



class SignUp(CreateView):
    form_class = UserCreateForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


def home(request):
    response = {}
    # users.objects.create(username = "kiwi", password = make_password("kiwi",salt="nothing"), email="kiwi@google.com", firstname = "kiwi", lastname = "kiwi", organisation = "kiwi")
    # response['data'] = request.user
    return render(request, "home.html", response)


def report_bug(request):
    if not request.user.is_authenticated:
        return reverse_lazy('login')
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bug = bugs()
            bug.title = form.cleaned_data['title']
            bug.bug = form.cleaned_data["bug"]
            bug.tags = form.cleaned_data["tags"]
            bug.date_created = datetime.now()
            bug.reporter = request.user
            bug.save()
            print(bug)
            return redirect('home')
    else:
        form = BugForm()

    context = {"form": form}
    return render(request, "report.html", context)


def view_bug(request, pk):
    bug = get_object_or_404(bugs, pk=pk)

    context = {"bug": bug}
    return render(request, "bug.html", context)


def register_teamcode(request):
    return render(request, "register_teamcode.html")


def dashboard(request):
    all_bugs = bugs.objects.all()
    context = {"bugs": all_bugs}
    return render(request, "bugs_dashboard.html", context)


def org(request, pk):
    response = {}
    response['organisations'] = get_object_or_404(organisation, pk=pk)
    return render(request, "bugs.html", response)

def software(request, pk):
    response = {}
    org = get_object_or_404(organisation, pk)
    if org :
        soft = org.software_ids.split(" ")
        response['softwares'] = softwares.objects.filter(UID__in = soft)
        return render(request, "display.html", response)

