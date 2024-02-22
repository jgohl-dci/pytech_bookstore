from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/store')

    elif request.method == "GET":
        form = RegistrationForm()

    return render(request, "user/registration.html", {"form": form})


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("/store")
            else:
                return render(request, "user/login.html", {"form": form})
        else:
            return render(request, "user/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/store")
