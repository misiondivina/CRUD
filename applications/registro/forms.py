from django import forms
from .models import DocenteCla

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