from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField('Genero')
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField()
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.libro.titulo} por {self.usuario.username}"

