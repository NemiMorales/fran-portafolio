from rest_framework.routers import DefaultRouter

from .views_api import CategoriaViewSet, CreacionViewSet


router = DefaultRouter()
router.register(
    r"creaciones",
    CreacionViewSet,
    basename="creacion",
)

router.register(r"categorias", CategoriaViewSet, basename="categoria")

urlpatterns = router.urls
