# Generated by Django 5.0 on 2023-12-15 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0002_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de reservacion')),
                ('fecha_checkIn', models.DateField(verbose_name='Fecha check in segun reserva')),
                ('fecha_checkOut', models.DateField(verbose_name='Fecha check out segun reserva')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.guest', verbose_name='Huespede/es de la reserva')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room', verbose_name='Habitacion de la reserva')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='CheckInOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(verbose_name='Fecha check in al hotel')),
                ('check_out', models.DateField(verbose_name='Fecha check out al hotel')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto total de la instancia')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation', verbose_name='Habitacion reservada')),
            ],
            options={
                'verbose_name': 'Check',
                'verbose_name_plural': 'Checks',
            },
        ),
    ]
