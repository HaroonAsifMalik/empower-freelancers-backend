from django.urls import path
from .views import TipListView

urlpatterns = [
    path('tips/', TipListView.as_view(), name='tip-list'),
]
