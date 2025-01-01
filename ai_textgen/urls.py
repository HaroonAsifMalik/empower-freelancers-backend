from django.urls import include, path
from ai_textgen.views import interact_with_ollama

urlpatterns = [
    path("generate-text/", interact_with_ollama, name="generate_text"),
]
