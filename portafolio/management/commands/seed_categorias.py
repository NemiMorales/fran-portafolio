from django.core.management.base import BaseCommand
from django.db import transaction
from portafolio.models import Categoria

CATEGORIAS = [
    ("Bombones de autor", "Bombonería fina y rellenos de autor."),
    ("Tabletas de origen", "Tabletas elaboradas con cacao de distintos orígenes."),
    ("Esculturas en chocolate", "Piezas artísticas y decorativas en chocolate."),
    ("Postres de restaurante", "Postres de carta y alta cocina."),
    ("Pastelería", "Repostería artesanal y pastelería de vitrina."),
]

class Command(BaseCommand):
    help = "Carga las categorías del diseño sin duplicar ni modificar las existentes."

    @transaction.atomic
    def handle(self, *args, **options):
        for nombre, descripcion in CATEGORIAS:
            categoria, created = Categoria.objects.get_or_create(
                nombre=nombre, defaults={"descripcion": descripcion}
            )
            self.stdout.write(f"{categoria.pk}: {nombre} ({'creada' if created else 'existente'})")
