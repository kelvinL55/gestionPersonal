from django import forms
from .models import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['codigo', 'nombre', 'ubicacion']
        labels = {
            'numero': 'N°',
            'codigo': 'Código',
            'nombre': 'Nombre',
            'ubicacion': 'Ubicación',
        }
        