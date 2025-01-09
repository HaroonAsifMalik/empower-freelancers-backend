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
    objects = CustomUserManager()
    image = models.ImageField(upload_to="user_images/", blank=True, null=True, default=RandomAvatar())
    def __str__(self):
        return self.email


