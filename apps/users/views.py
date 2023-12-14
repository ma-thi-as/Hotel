from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from .models import User
from .forms import CustomUserRegister
# Create your views here.

class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        messages.success(self.request, 'Login exitoso')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Email o constraseña incorrectos')
        return super().form_invalid(form)


    def get_success_url(self):
        return '/'

class IndexView(TemplateView):
    template_name = "index.html"


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserRegister
    template_name = "register.html"
    success_url = reverse_lazy('users:login')
