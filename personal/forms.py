from django import forms
from .models import Personal

class PersonalForm(forms.ModelForm):
    """
    Formulario para la creación y edición de registros de Personal
    """
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
        error_messages = {
            'codigo': {
                'unique': 'Ya existe un registro con este código en el sistema.'
            }
        }
