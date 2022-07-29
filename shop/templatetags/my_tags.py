from django import template

register = template.Library()
from shop.models import WishlistModel, ProductModel


@register.simple_tag()
def get_current_price(request, x):
    data = request.GET.get('price')
    if data:
        return data.split(';')[x]
    else:
        return 'null'


@register.simple_tag()
def cart_info(request):
    return ProductModel.get_cart_info(request)


@register.filter()
def is_wishlist(product, request):
    return WishlistModel.objects.filter(user=request.user, product=product).exists()


@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])
