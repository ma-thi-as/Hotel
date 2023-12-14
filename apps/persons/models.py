from django.db import models
from apps.users.models import User

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True) # Validators should be a list
    direction = models.CharField("Direccion", max_length=50)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} doc: {self.document}'

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
