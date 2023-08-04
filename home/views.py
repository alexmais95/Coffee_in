from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Coffee, Category
from .utils import DataMixin
from .forms import *


class BleacCoffee(DataMixin, ListView):
    model = Coffee
    template_name = 'home/blaccoffee.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Чиста кава')
        return context | c_def

    def get_queryset(self):
        return Coffee.objects.filter(cat_id=1)


class WithMilk(DataMixin, ListView):
    model = Coffee
    template_name = 'home/with_milk.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Кава з молоком')
        return context | c_def

    def get_queryset(self):
        return Coffee.objects.filter(cat_id=2)


class ShowPost(DataMixin, DetailView):
    model = Coffee
    template_name = 'home/post.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Описання')
        return dict(list(context.items()) + list(c_def.items()))



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
