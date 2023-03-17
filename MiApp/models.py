from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion_titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length= 150)

    def __str__(self) :
        return f"{self.id} - {self.titulo}"




