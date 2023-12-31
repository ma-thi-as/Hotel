# Generated by Django 5.0 on 2023-12-15 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monoto total del pago')),
                ('payment_day', models.DateField(verbose_name='Fecha de pago')),
                ('payment_type', models.CharField(choices=[('efectivo', 'efectivo'), ('credito', 'tarjeta de credito'), ('debito', 'tarjeta de debito')], max_length=50)),
                ('checkInOut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.checkinout', verbose_name='Check in/out')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation', verbose_name='Reservacion')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
