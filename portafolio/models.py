from django.db import models

class Contacto(models.Model):
    email = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
   
    def __str__(self):
        return self.email


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    contacto = models.ForeignKey(
    Contacto,
    on_delete = models.CASCADE,
    related_name="contacto"
    )
    descripcion = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
  
    def __str__(self):
        return self.nombre

class Creacion(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
    Categoria,
    on_delete = models.CASCADE,
    related_name="creaciones"
    )
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

class ExperienciasAdicionales(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Conocimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Idioma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    