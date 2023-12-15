from django.apps import AppConfig
from django.db.models.signals import post_save

class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.persons'

    def ready(self):
        from apps.users.models import User
        from .receivers import crear_user_bassedOnAttrs, save_user_bassedOnAttrs

        post_save.connect(crear_user_bassedOnAttrs, sender= User)
        post_save.connect(save_user_bassedOnAttrs, sender= User)