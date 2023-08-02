from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Coffee, Category
from .utils import DataMixin
from .forms import *


def blaccoffee(request):
    item = Coffee.objects.all()
    return render(request, 'home/blaccoffee.html', {'item': item, 'title': 'Bleak coffee'})


def with_milk(request):
    item = Coffee.objects.all()
    return render(request, 'home/with_milk.html', {'item': item, 'title': 'Coffee with milk'})


# def login(request):
#     return render(request, 'home/login.html', {'title': 'login'})


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")

# def show_category(request, cat_id):
#     posts = Coffee.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регістрація користувача')
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('blaccoffee')


def logout_user(request):
    logout(request)
    return redirect('login')
