from django.db import models
from apps.reservations.models import Reservation, CheckInOut
# Create your models here.
class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, verbose_name="Reservacion", on_delete=models.CASCADE)
    checkInOut = models.ForeignKey(CheckInOut, verbose_name="Check in/out", on_delete=models.CASCADE)
    total_amount = models.DecimalField("Monoto total del pago", max_digits=10, decimal_places=2)
    payment_day = models.DateField("Fecha de pago", auto_now=False, auto_now_add=False)
    payment_options = [('efectivo', 'efectivo'),('credito','tarjeta de credito'),('debito','tarjeta de debito')]
    payment_type = models.CharField(max_length=50, choices=payment_options)
    

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f'{self.reservation}'

    def get_absolute_url(self):
        return reverse("payments:detail", kwargs={"pk": self.pk})
