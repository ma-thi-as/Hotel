# forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = Employee
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        # Puedes acceder al modelo actual a través de self.instance
        # y luego acceder al campo email del modelo
        if self.instance and self.instance.user:
            self.initial['email'] = self.instance.user.email

    # Ejemplo: Agregar un widget específico para el campo phone_number
    widgets = {
        'phone_number': forms.TextInput(attrs={'placeholder': 'Escribe tu número de teléfono'}),
    }
    def save(self, commit =True):
        emp = super(EmployeeForm, self).save(commit=True)
        
        user = emp.user
        user.email = self.cleaned_data['email']

        if commit:
            emp.save()
            user.save()

        return emp


