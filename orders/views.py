from django.shortcuts import render, reverse
from django.views.generic import CreateView, TemplateView
from .models import OrderHistoryModel
from .forms import CheckoutForm
from shop.models import ProductModel
from users.models import ProfileModel


class CheckoutView(CreateView):
    model = OrderHistoryModel
    template_name = 'checkout.html'
    form_class = CheckoutForm

    def get_success_url(self):
        return reverse('orders:history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = ProductModel.get_cart_objects(self.request)


        if hasattr(self.request.user, 'profiles'):
            context['profile'] = self.request.user.profiles

        return context



class OrderHistoryView(TemplateView):
    template_name = 'order_history.html'
