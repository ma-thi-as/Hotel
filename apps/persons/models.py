from django.db import models
from django.core.validators import RegexValidator
from apps.users.models import User

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True) # validar formato del numero con regex tiene que estar en un alista en validaores
    direction = models.CharField("Direccion", max_length=50)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        
        return f'{self.user.first_name} {self.user.last_name} doc: {self.user.document}' 
        
    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})



class Guest(models.Model):
    user = models.OneToOneField(User, verbose_name="Huesped del hotel", on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.") # formato y longitud de 12 caracteres
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True) # validar formato del numero con regex tiene que estar en un alista en validaores
    direction = models.CharField("Direccion", max_length=50)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} doc: {self.user.document}'

    def get_absolute_url(self):
        return reverse("Guest_detail", kwargs={"pk": self.pk})
