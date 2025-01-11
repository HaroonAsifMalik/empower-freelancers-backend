import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dotenv import load_dotenv
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignIn, LogOut, SignUp, UserInfo

load_dotenv()

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', LogOut.as_view(), name='sign-out'),
    path('user-info/', UserInfo.as_view(), name='user-info'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

]

