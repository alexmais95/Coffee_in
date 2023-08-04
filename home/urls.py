from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('bleaccoffee/', BleacCoffee.as_view(), name='blaccoffee'),
    path('with_milk/', WithMilk.as_view(), name='with_milk'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:slug>/', ShowPost.as_view(), name='post'),

]