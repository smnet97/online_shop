from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductTagModel, ProductModel, CategoryModel, SizeModel, ColorModel, BrandModel
from .forms import ColorModelAdminForms

@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'color']
    list_display_links = ['code']
    search_fields = ['code']
    form = ColorModelAdminForms

    def color(self, obj):
        free_space = '&nbsp;' * 5
        return mark_safe(f"<div style='background-color:{obj.code}; width:200px;'>{free_space}</div>")


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
