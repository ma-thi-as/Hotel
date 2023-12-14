from django.db import models

# Create your models here.

class Room_type(models.Model):

    type_name = models.CharField("Nombre del tipo de habitacion", max_length=50)
    detail = models.TextField("Detalle del tipo")

    class Meta:
        verbose_name = "Room type"
        verbose_name_plural = "Room types"

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("Room_type_detail", kwargs={"pk": self.pk})


class Room(models.Model):

    room_number = models.PositiveSmallIntegerField("Numero de la habitacion" )
    floor = models.PositiveSmallIntegerField("Piso de la habitacion")
    night_price = models.DecimalField("Precio de la habitacion", max_digits=10, decimal_places=2)
    description = models.TextField("Descripcion de la habitacion")
    state_choices = [('libre', 'sin huesped'), ('ocupada', 'con huesped'), ('rentada', 'pagada pero sin huesped'), ('no', 'no disponible')]
    state = models.CharField(choices = state_choices)
    room_type = models.ForeignKey(Room_type, verbose_name="Tipo habitacion", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_number

    def get_absolute_url(self):
        return reverse("Room_detail", kwargs={"pk": self.pk})
