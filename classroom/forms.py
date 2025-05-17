
from django import forms
from .models import Curso, Tarea, Entrega

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_entrega']

class CalificarEntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['calificacion', 'retroalimentacion']
