from django import forms
from .models import OrderHistoryModel


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = OrderHistoryModel
        exclude = ['user', 'products', 'created_at']
