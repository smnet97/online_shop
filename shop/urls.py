from django.urls import path
from .views import ShopView, ProductDetailView, wishlist_view, WishlistListView, update_cart_view

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/wishlist/', wishlist_view, name='wishlist'),
    path('wishlists/', WishlistListView.as_view(), name='all_wishlist'),
    path('add_cart/<int:id>/', update_cart_view, name='cart')
]

