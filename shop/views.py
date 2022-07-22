from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductModel


class ShopView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self):
        return ProductModel.objects.all()
