import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def home(request):
    ruta_json = (
        Path(settings.BASE_DIR)
        / "portafolio"
        / "data"
        / "fran.json"
    )

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return render(
        request,
        "portafolio/home.html",
        {"datos": datos}
    )