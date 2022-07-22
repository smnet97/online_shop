from django.urls import path
from .views import ShopView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail')
]
