from django.urls import path
from .views import ProjectsView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects_list_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
