from rest_framework import mixins, permissions, viewsets

from .models import Creacion
from .serializers import CreacionSerializer


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