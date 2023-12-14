from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee

@receiver(post_save, sender=User)
def crear_usario_employee(sender, instance, created, **kwargs):
        if created:
            Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_usuario_employee(sender, instance, **kwargs):
    
    instance.employee.save()