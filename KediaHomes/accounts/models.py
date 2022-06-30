from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *


class User(AbstractUser):
    name = models.CharField(max_length=50, default="NA")
    username = None
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)
    is_mobile = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    key = models.TextField(max_length=20000, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='User/', blank=True, null=True)
    token = models.TextField(max_length=20000, null=True, blank=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile', 'updated_at', 'is_mobile', 'is_email', 'key']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "User"

    @staticmethod
    def emailExists(email):
        if User.objects.filter(email=email):
            return True
        return False
    
    @staticmethod
    def mobileExists(mobile):
        if User.objects.filter(mobile=mobile):
            return True
        return False