from django.apps import AppConfig


class JsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jsapp'
    
    def ready(self):
        from .ap_scheduler import start
        start()