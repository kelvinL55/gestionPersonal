from django.db import models

class Personal(models.Model):
    numero = models.PositiveIntegerField(unique=True)  # Este será tu campo "N°"
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.numero:  # Si el número no está asignado
            last_num = Personal.objects.order_by('numero').last()  # Obtener el último número
            if last_num:
                self.numero = last_num.numero + 1  # Asignar el siguiente número
            else:
                self.numero = 1  # Si es el primer registro
        super().save(*args, **kwargs)
