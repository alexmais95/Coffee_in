from django.contrib import admin

from .models import Coffee, Category


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cat_id', 'time_create',  'photo']
    list_display_links = ['id', 'title', 'cat_id']
    search_fields = ['title', 'content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Category, CategoryAdmin)
