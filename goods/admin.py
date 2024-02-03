from django.contrib import admin

from goods.models import Categories, Products


# Регистрация класса категорий
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Поля зполняемые автоматически
    prepopulated_fields = {"slug": ("name",)}


# Регистрация класса продукт
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # Поля зполняемые автоматически
    prepopulated_fields = {"slug": ("name",)}
