from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "gestion/creaciones/",
        views.CreacionListView.as_view(),
        name="gestion-creaciones",
    ),
    path(
    "gestion/creaciones/nueva/",
    views.CreacionCreateView.as_view(),
    name="gestion-creacion-nueva",
    ),
    path(
    "gestion/creaciones/<int:pk>/editar/",
    views.CreacionUpdateView.as_view(),
    name="gestion-creacion-editar",
    ),
    path(
    "gestion/creaciones/<int:pk>/toggle/",
    views.toggle_creacion,
    name="gestion-creacion-toggle",
    ),
    path(
    "gestion/creaciones/<int:pk>/toggle/",
    views.toggle_creacion,
    name="gestion-creacion-toggle",
    ),
]