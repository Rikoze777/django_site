from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User
from django.urls import reverse


def get_customers(request):
    data = User.objects.filter(role="customer")
    return render(request, "customers.html", {"data": data})


def get_perfomers(request):
    data = User.objects.filter(role="perfomer")
    return render(request, "perfomers.html", {"data": data})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})


def index(request):
    return render(request, "index.html")
