from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('', views.blaccoffee, name='blaccoffee'),
    path('with_milk/', views.with_milk, name='with_milk'),

]