from django.db import models
from django.urls import reverse
# Create your models here.

class Room_type(models.Model):

    type_name = models.CharField("Nombre del tipo de habitacion",max_length=50)
    detail = models.TextField("Detalle del tipo")

    class Meta:
        verbose_name = "Room type"
        verbose_name_plural = "Room types"

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("rooms:type_detail", kwargs={"pk": self.pk})


class Room(models.Model):

    room_number = models.SmallIntegerField()
    floor = models.PositiveSmallIntegerField("Piso de la habitacion")
    night_price = models.DecimalField("Precio de la habitacion", max_digits=10, decimal_places=2)
    description = models.TextField("Descripcion de la habitacion")
    state_choices = [('libre', 'sin huesped'), ('ocupada', 'con huesped'), ('rentada', 'pagada pero sin huesped'), ('no', 'no disponible')]
    state = models.CharField(max_length=50,choices = state_choices)
    room_type = models.ForeignKey(Room_type, verbose_name="Tipo habitacion", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return f'numero: {self.room_number} | piso:{self.floor}'

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
