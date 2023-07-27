from django.http import HttpResponse
from django.shortcuts import render
from .models import Coffee, Category


def blaccoffee(request):
    item = Coffee.objects.all()
    return render(request, 'home/blaccoffee.html', {'item': item, 'title': 'Bleak coffee'})


def with_milk(request):
    item = Coffee.objects.all()
    return render(request, 'home/with_milk.html', {'item': item, 'title': 'Coffee with milk'})

# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")

# def show_category(request, cat_id):
#     posts = Coffee.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()