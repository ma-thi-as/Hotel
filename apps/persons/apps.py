from django.apps import AppConfig
from django.db.models.signals import post_save

class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.persons'

    def ready(self):
        from apps.users.models import User
        from .receivers import crear_usario_employee, save_usuario_employee

        post_save.connect(crear_usario_employee, sender= User)
        post_save.connect(save_usuario_employee, sender= User)