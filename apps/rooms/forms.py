from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'floor', 'night_price', 'description', 'state', 'room_type']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si es necesario
        # Por ejemplo, puedes agregar validadores o widgets específicos
