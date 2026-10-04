from rest_framework import serializers

from .models import Creacion


class CreacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creacion
        fields = "__all__"