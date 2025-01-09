from django.urls import include, path
from ai_textgen.views import interact_with_ollama, run_web_scrap

urlpatterns = [
    path("generate-text/", interact_with_ollama, name="generate_text"),
    path('jobs/', run_web_scrap, name='extract_job'),
]
