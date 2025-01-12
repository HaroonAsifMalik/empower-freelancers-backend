from django.contrib import admin
from django.urls import include, path
import os
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv


api_v1_patterns = [
    path("accounts/", include("accounts.urls")),
    path("projects/", include("projects.urls")),
    path("ai_textgen/", include("ai_textgen.urls")),
    path("guidance/", include("guidance.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include((api_v1_patterns, "api_v1"), namespace="api_v1")),
]


if os.environ["DJANGO_SETTINGS_MODULE"] == "core.settings.development":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
