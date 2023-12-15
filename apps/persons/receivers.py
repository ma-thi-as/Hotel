from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee, Guest

@receiver(post_save, sender=User)
def crear_user_bassedOnAttrs(sender, instance, created, **kwargs):
    """ Receiver para craer un empleado u  """

    if instance.is_superuser or instance.is_staff :
        if created:
            Employee.objects.create(user=instance)
            
    else:
        if created:
            Guest.objects.create(user=instance)
            
@receiver(post_save, sender=User)
def save_user_bassedOnAttrs(sender, instance, **kwargs):
    # Utilizar el manager relacionado para evitar problemas con getattr
    employee_instance = instance.employee if hasattr(instance, 'employee') else None
    guest_instance = instance.guest if hasattr(instance, 'guest') else None

    if employee_instance:
        # El usuario tiene un objeto Employee asociado
        employee_instance.save()

    if guest_instance:
        guest_instance.save()
