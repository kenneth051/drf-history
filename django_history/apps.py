from django.apps import AppConfig


class django_historyConfig(AppConfig):
    name = "django_history"

    def ready(self):
        import django_history.signals
