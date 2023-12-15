from django.apps import AppConfig


class ApiLycsFidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_lycs_fid'
    def ready(self):
        import api_lycs_fid.signals