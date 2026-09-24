
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView
from django.views.decorators.http import require_POST
from portafolio.forms import CreacionForm
from .models import Creacion
import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/admin/login/")
@require_POST
def toggle_creacion(request, pk):
    creacion = get_object_or_404(Creacion, pk=pk)

    creacion.activo = not creacion.activo
    creacion.save(update_fields=["activo"])

    return redirect("gestion-creaciones")

def home(request):
    ruta_json = (
        Path(settings.BASE_DIR)
        / "portafolio"
        / "data"
        / "fran.json"
    )

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    creaciones = (
        Creacion.objects
        .filter(activo=True)
        .select_related("categoria")
    )

    return render(
        request,
        "portafolio/home.html",
        {
            "datos": datos,
            "creaciones": creaciones,
        }
    )

class CreacionListView(LoginRequiredMixin, ListView):
    model = Creacion
    template_name = "portafolio/gestion/creaciones_lista.html"
    context_object_name = "creaciones"
    login_url = "/admin/login/"

    def get_queryset(self):
        return Creacion.objects.select_related('categoria').order_by('pk')


class CreacionModalMixin:
    def get_template_names(self):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return ['portafolio/gestion/_creacion_form.html']
        return super().get_template_names()

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Creación guardada correctamente.')
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'redirect': str(self.success_url)})
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response.status_code = 422
        return response

class CreacionCreateView(LoginRequiredMixin, CreacionModalMixin, CreateView):
    model = Creacion
    form_class = CreacionForm
    template_name = "portafolio/gestion/creacion_form.html"
    success_url = reverse_lazy("gestion-creaciones")
    login_url = "/admin/login/"

class CreacionUpdateView(LoginRequiredMixin, CreacionModalMixin, UpdateView):
    model = Creacion
    form_class = CreacionForm
    template_name = "portafolio/gestion/creacion_form.html"
    success_url = reverse_lazy("gestion-creaciones")
    login_url = "/admin/login/"