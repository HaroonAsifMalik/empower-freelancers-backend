from django.apps import AppConfig


class AiTextgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_textgen'

    def ready(self):
        import ai_textgen.signals
