from django.contrib import admin
from .models import Blog, Tag, Category


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']
