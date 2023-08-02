from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('blaccoffee/', views.blaccoffee, name='blaccoffee'),
    path('with_milk/', views.with_milk, name='with_milk'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

]