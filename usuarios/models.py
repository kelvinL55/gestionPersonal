from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """
    Modelo que extiende el usuario estándar de Django con campos adicionales.
    
    Attributes:
        usuario (User): Relación uno a uno con el modelo User de Django
        telefono (str): Número de teléfono del usuario
        fecha_nacimiento (date): Fecha de nacimiento del usuario
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
