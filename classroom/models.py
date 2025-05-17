

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos_creados')
    estudiantes = models.ManyToManyField(User, related_name='cursos_inscritos', blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateTimeField()
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Entrega(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/')
    entregado_en = models.DateTimeField(auto_now_add=True)
    calificacion = models.FloatField(null=True, blank=True)
    retroalimentacion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.estudiante.username} - {self.tarea.titulo}"

