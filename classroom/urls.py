from django.urls import path, include
from . import views

urlpatterns = [
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/<int:curso_id>/tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/entregas/', views.ver_entregas, name='ver_entregas'),
    path('entregas/<int:entrega_id>/calificar/', views.calificar_entrega, name='calificar_entrega'),
]
