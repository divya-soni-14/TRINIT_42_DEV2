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

from .forms import BugForm, ApproveForm, UserCreateForm
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
    # if(request.user.is_authenticated):
    #     userDet = userDetail.get(user = request.user)
    #     if not userDet:
    #         userDetail.objects.create(access_level="0", user=request.user)
    # users.objects.create(username = "kiwi", password = make_password("kiwi",salt="nothing"), email="kiwi@google.com", firstname = "kiwi", lastname = "kiwi", organisation = "kiwi")
    # response['data'] = request.user
    return render(request, "home.html", response)


def report_bug(request):
    if not request.user.is_authenticated:
        return reverse_lazy("login")
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            bug = bugs()
            bug.title = form.cleaned_data["title"]
            bug.bug = form.cleaned_data["bug"]
            bug.tags = form.cleaned_data["tags"]
            bug.date_created = datetime.now()
            bug.reporter = request.user
            bug.save()
            print(bug)
            return redirect("home")
    else:
        form = BugForm()

    context = {"form": form}
    return render(request, "report.html", context)


def view_bug(request, pk):
    bug = get_object_or_404(bugs, pk=pk)

    context = {"bug": bug}
    return render(request, "bug.html", context)


def approve_bug(request, pk):
    bug = get_object_or_404(bugs, pk=pk)
    if request.method == "POST":
        form = ApproveForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            redirect("dashboard")
            # title = form.cleaned_data["title"]
            # bug = form.cleaned_data["bug"]
            # tags = form.cleaned_data["tags"]
            # print(title, bug, tags)
    else:
        form = ApproveForm()
    context = {"bug": bug, "form": form}

    return render(request, "approve.html", context)


def register_teamcode(request):
    return render(request, "register_teamcode.html")


def dashboard(request):
    user = request.user
    # userDet = userDetail.objects.get(user=user)
    # print(userDet.access_level)
    all_bugs = bugs.objects.all()
    context = {"bugs": all_bugs}
    is_pub = False
    # for bug in all_bugs:
    #     is_pub = bug.is_public
    #     if(is_pub):
    #         finalBugs.append()

       
        
    return render(request, "bugs_dashboard.html", context)


def org(request, pk):
    response = {}
    response["organisations"] = get_object_or_404(organisation, pk=pk)
    return render(request, "bugs.html", response)


def software(request, pk):
    response = {}
    org = get_object_or_404(organisation, pk)
    if org:
        soft = org.software_ids.split(" ")
        response["softwares"] = softwares.objects.filter(UID__in=soft)
        return render(request, "display.html", response)
