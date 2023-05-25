from django.apps import AppConfig

class MusicEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'music_engine'

    def ready(self):
        import django.core.signals
