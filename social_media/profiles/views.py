import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from profiles.forms import RegisterForm, LoginForm

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("my_page")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def my_page(request):
    return render(request, "my_page.html", {"form": form})
