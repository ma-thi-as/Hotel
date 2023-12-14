from django.test import TestCase
from .receivers import crear_usario_employee
from django.core.management import call_command

from apps.users.models import User
from .models import Employee
from .receivers import save_usuario_employee

class EmployeeSignalsTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para usar en las pruebas
        call_command('flush', '--noinput')
        self.user = User.objects.create_superuser(first_name='atun',last_name='queso', email='test@example.com', password='testpass')
        self.normal_user = User.objects.create_user(first_name='vainilla',last_name='valentina', email='gg@example.com', password='testpass')

    def test_employee_created_on_user_creation(self):
        # Asegurar que no haya un Employee antes de la señal
        #self.assertFalse(Employee.objects.filter(user=self.user).exists())
        self.assertEqual(True, Employee.objects.filter(user=self.user).exists())
        print(Employee.objects.filter(user=self.user).exists())

        # Asegurar que un Employee fue creado después de la señal
        

    def test_employee_update_post_save(self):
        print(Employee.objects.update_or_create(phone_number='312123123', direction='quilikumbia'))