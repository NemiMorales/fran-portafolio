from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portafolio.urls")),
    path("api/", include("portafolio.api_urls")),
]