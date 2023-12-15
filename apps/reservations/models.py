from django.db import models
from apps.persons.models import Guest
from apps.rooms.models import Room
from django.urls import reverse
# Create your models here.

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, verbose_name="Huespede/es de la reserva", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Habitacion de la reserva", on_delete=models.CASCADE)
    reservation_date = models.DateField("Fecha de reservacion", auto_now=False, auto_now_add=True)
    fecha_checkIn = models.DateField("Fecha check in segun reserva", auto_now=False, auto_now_add=False)
    fecha_checkOut = models.DateField("Fecha check out segun reserva", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f'Huesped: {self.guest} | Habitacion: {self.room}'

    def get_absolute_url(self):
        return reverse("reservations:detail", kwargs={"pk": self.pk})

class CheckInOut(models.Model):
    reservation = models.ForeignKey(Reservation, verbose_name="Habitacion reservada", on_delete=models.CASCADE)
    check_in = models.DateField("Fecha check in al hotel", auto_now=False, auto_now_add=False)
    check_out = models.DateField("Fecha check out al hotel", auto_now=False, auto_now_add=False)
    total_amount = models.DecimalField("Monto total de la instancia", max_digits=10, decimal_places=2)    

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"

    def __str__(self):
        return f'{self.reservation}'

    def get_absolute_url(self):
        return reverse("reservations:check_detail", kwargs={"pk": self.pk})

