from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import DocenteCla
from .models import Materia
from .models import NoDocente
from .models import Oficina
from .forms import DocenteForm

# Create your views here.

class DocenteListViewAll(ListView):
    model = DocenteCla
    template_name = "registro/list_all.html"
    ordering = 'Apellido'
    context_object_name = 'lista'
    paginate_by = 4
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = DocenteCla.objects.filter(
            Apellido__icontains = palabra_clave
        )
        return lista

class MateriaListViewAll(ListView):
    model = Materia
    template_name = "registro/list_materia.html"
    ordering = 'MNombre'
    context_object_name = 'listaMateria'
    paginate_by = 4

class NoDocenteListViewAll(ListView):
    model = NoDocente
    template_name = "registro/list_allNoDoc.html"
    ordering = 'NApellido'
    context_object_name = 'listaND'
    paginate_by = 4

class OficinaListViewAll(ListView):
    model = Oficina
    template_name = "registro/list_oficina.html"
    ordering = 'ONombre'
    context_object_name = 'listaOficina'
    paginate_by = 4


class DocenteListViewAllBuscar(ListView):
    model = DocenteCla
    template_name = "registro/buscarD.html"
    ordering = 'Apellido'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('QDocente', '')
        lista = DocenteCla.objects.filter(
        Apellido = palabra_clave
        )
        return lista

class SuccessView(TemplateView):
    template_name = "registro/exito.html"

class DocenteCreateView(CreateView):
    model = DocenteCla
    template_name = "registro/altaD.html"
    form_class = DocenteForm

    success_url = reverse_lazy ('registro_app:listar-todo')
class DocenteUpdateView(UpdateView):
    model = DocenteCla
    template_name = "registro/modifD.html"
    form_class = DocenteForm

    success_url = reverse_lazy ('registro_app:listar-todo')

class DocenteDeleteView(DeleteView):
    model = DocenteCla
    template_name = "registro/borrarD.html"
    form_class = DocenteForm

    success_url = reverse_lazy ('registro_app:listar-todo')

class DocenteDetalleView(DetailView):
    model = DocenteCla
    template_name = "registro/detalle.html"
    form_class = DocenteForm
    context_object_name = 'detalle'

class VistaPrincipal(TemplateView):
    template_name = "index.html"