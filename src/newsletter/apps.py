from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'

    def ready(self) -> None:
        from newsletter import signals
        return super().ready()
