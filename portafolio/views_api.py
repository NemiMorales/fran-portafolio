from rest_framework import mixins, permissions, viewsets

from .models import Categoria, Creacion
from .serializers import CategoriaSerializer, CreacionSerializer


class CreacionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Creacion.objects.all().order_by("-id")
    serializer_class = CreacionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all().order_by("nombre", "id")
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
