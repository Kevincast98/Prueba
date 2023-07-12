from django.db import models


# Create your models here.

#CREAMOS EL MODELO PERSONA
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='')
    tipo_documento = models.CharField(max_length=100, default='')
    numero_documento = models.CharField(max_length=100, default='')
    correo = models.EmailField(max_length=254, default='')
    telefono = models.CharField(max_length=20, default='')
    # Otros campos que desees agregar

    def __str__(self):
        return self.nombre

    

#CREAMOS EL MODELO TAREA
class Tarea(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()

    def __str__(self):
        return self.titulo