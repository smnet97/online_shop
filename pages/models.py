from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    massage = models.TextField(verbose_name=_('massage'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'