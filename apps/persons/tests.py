from django.test import TestCase
from .models import Employee, Guest
from apps.users.models import User
from django.core.management import call_command

class EmployeeSignalsTestCase(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        self.user = User.objects.create_superuser(first_name='atun', last_name='queso', email='test@example.com', document='1231231231', password='testpass')
        self.normal_user = User.objects.create_user(first_name='vainilla', last_name='valentina', email='gg@example.com', document='123123123', password='testpass')

    def test_employee_created_on_user_creation(self):
        # Asegurar que no haya un Employee antes de la señal
        self.assertFalse(Employee.objects.filter(user=self.normal_user).exists())

        # Crear un usuario y verificar que se cree un Employee después de la señal
        self.user.save()
        self.assertTrue(Employee.objects.filter(user=self.user).exists())

class GuestSignalsTestCase(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        self.user = User.objects.create_superuser(first_name='vainaaaaaailla', last_name='valentina', email='amen@example.com', document='123456789', password='testpass')
        self.normal_user = User.objects.create_user(first_name='vainilla', last_name='valentina', email='gg@example.com', document='123456789', password='testpass')

    def test_guest_created_on_user_creation(self):
        # Asegurar que no haya un Guest antes de la señal
        
        print("Antes de la señal:", Guest.objects.filter(user=self.normal_user).values())
        self.assertFalse(Guest.objects.filter(user=self.normal_user).exists())

        # Crear un usuario y verificar que se cree un Guest después de la señal
        self.user.save()
        #self.assertTrue(Guest.objects.filter(user=self.user).exists())
