from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser



admin.site.register(CustomUser)
