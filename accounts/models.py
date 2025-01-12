from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager
from django.utils.deconstruct import deconstructible
import random




@deconstructible
class RandomAvatar:
    def __init__(self):
        self.avatar = [
            "avatars/1.png",
            "avatars/2.png",
            "avatars/3.png",
            "avatars/4.png",
            "avatars/5.png",
        ]

    def __call__(self):
        return random.choice(self.avatar)


class CustomUser(AbstractUser):
    username = None
    display_name = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']
    
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="user_images/", blank=True, null=True, default=RandomAvatar())
    accounts = models.JSONField(default=list, blank=True)
    response_time = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    job_success_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    skills = models.JSONField(default=list, blank=True)
    categories = models.JSONField(default=list, blank=True)
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_image_url(self):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image.url}"
        return None
