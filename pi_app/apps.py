from django.apps import AppConfig


class PiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pi_app'


    def ready(self) -> None:
        from . import signals