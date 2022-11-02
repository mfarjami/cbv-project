# from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class LoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"


class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("todo:index")
    form_class = UserCreationForm
