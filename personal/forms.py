from django import forms
from .models import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['codigo', 'nombre', 'ubicacion', 'grupo', 'categorias']
        labels = {
            'numero': 'N°',
            'codigo': 'Código',
            'nombre': 'Nombre',
            'ubicacion': 'Ubicación',
            'grupo': 'G - GRUPO',
            'categorias': 'Categorías',
        }
        