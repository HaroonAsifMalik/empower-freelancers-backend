from django.urls import include, path
from ai_textgen.views import run_web_scrap, AIProposalResponseListView, interact_with_ollama

urlpatterns = [
    path('ai-responses/', AIProposalResponseListView.as_view(), name='ai_responses'),
    path('jobs/', run_web_scrap, name='extract_job'),
    path('generate-text/', interact_with_ollama, name='interact_with_ollama'),

]
