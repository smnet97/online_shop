from django import forms
from .models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']
