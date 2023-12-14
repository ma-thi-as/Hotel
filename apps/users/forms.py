from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserRegister(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido ingrese un direccion correcta.")
    first_name = forms.CharField( max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']