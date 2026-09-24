from django.contrib import admin

from .models import (
    Categoria,
    Conocimiento,
    Contacto,
    Curso,
    Creacion,
    Especialidad,
    Estudio,
    Experiencia,
    ExperienciasAdicionales,
    Idioma,
    Logro,
    Perfil,
)


admin.site.register([
    Categoria,
    Conocimiento,
    Contacto,
    Curso,
    Creacion,
    Especialidad,
    Estudio,
    Experiencia,
    ExperienciasAdicionales,
    Idioma,
    Logro,
    Perfil,
])