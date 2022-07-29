from django import template

register = template.Library()
from shop.models import WishlistModel

@register.simple_tag()
def get_current_price(request, x):
    data = request.GET.get('price')
    if data:
        return data.split(';')[x]
    else:
        return 'null'

@register.filter()
def is_wishlist(product, request):
    return WishlistModel.objects.filter(user=request.user, product=product).exists()