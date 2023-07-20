from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def intro(request):
    return HttpResponse("You're looking at question")