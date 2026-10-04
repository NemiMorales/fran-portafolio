from rest_framework.routers import DefaultRouter

from .views_api import CreacionViewSet


router = DefaultRouter()
router.register(
    r"creaciones",
    CreacionViewSet,
    basename="creacion",
)

urlpatterns = router.urls