from rest_framework import serializers

from .models import Categoria, Creacion


class CreacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creacion
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nombre", "descripcion"]
