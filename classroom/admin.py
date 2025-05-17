

# Register your models here.

from django.contrib import admin
from .models import Curso, Tarea, Entrega

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'creado_en')
    search_fields = ('nombre', 'profesor__username')

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'fecha_entrega')
    search_fields = ('titulo', 'curso__nombre')

class EntregaAdmin(admin.ModelAdmin):
    list_display = ('tarea', 'estudiante', 'entregado_en', 'calificacion')
    search_fields = ('tarea__titulo', 'estudiante__username')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega, EntregaAdmin)
