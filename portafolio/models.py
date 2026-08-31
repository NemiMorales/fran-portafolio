from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Creacion(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


class Logro(models.Model):
    valor = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"