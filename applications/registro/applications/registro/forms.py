from django import forms
from .models import DocenteCla
from .models import NoDocente

class DocenteForm(forms.ModelForm):

    class Meta:
        model = DocenteCla
        template_name = "registro/modifD.html"
        fields = [
            'Nombre',
            'Apellido',
            'Edad',
            'materia',
        ]

class NoDocenteForm(forms.ModelForm):

    class Meta:
        model = NoDocente
        template_name = "registro/modifND.html"
        fields = [
            'NNombre',
            'NApellido',
            'NEdad',
            'oficina',
        ]