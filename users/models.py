from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)



    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


