from django import forms

from .models import Creacion


class CreacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Selecciona una categoría'

    class Meta:
        model = Creacion
        fields = [
            "nombre",
            "categoria",
            "descripcion",
            "imagen",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Bombón de chocolate amargo'}),
            'descripcion': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Técnica, ingredientes, origen del cacao...'}),
            'imagen': forms.URLInput(attrs={'placeholder': 'https://…'}),
        }
