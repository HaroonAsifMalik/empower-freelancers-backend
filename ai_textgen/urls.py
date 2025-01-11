from django.urls import include, path
from ai_textgen.views import run_web_scrap, AIProposalResponseListView

urlpatterns = [
    path('ai-responses/', AIProposalResponseListView.as_view(), name='ai_responses'),
    path('jobs/', run_web_scrap, name='extract_job'),
]
