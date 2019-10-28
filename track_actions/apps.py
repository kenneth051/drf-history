from django.apps import AppConfig


class track_actionsConfig(AppConfig):
    name = "track_actions"

    def ready(self):
        import track_actions.signals
