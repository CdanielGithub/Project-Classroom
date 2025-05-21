from django.urls import path
from . import views
from estudiante.views import CursosInscritosView,TareasPendientesView,EntregarTareaView,EntragaEditarEliminar,EntregaListCreateView

urlpatterns = [
    path("cursos/", views.listar_cursos, name="listar_cursos"),
    path("cursos/crear/", views.crear_curso, name="crear_curso"),
    path("cursos/<int:curso_id>/tareas/crear/", views.crear_tarea, name="crear_tarea"),
    path("tareas/<int:tarea_id>/entregas/", views.ver_entregas, name="ver_entregas"),
    path(
        "entregas/<int:entrega_id>/calificar/",
        views.calificar_entrega,
        name="calificar_entrega",
    ),
    path("auth/login/", views.login, name="login"),
    path("auth/signup/", views.registrar_usuario, name="login"),
    path("auth/refresh/", views.refresh_token),

    #estudiante
    path('cursos_inscrito/', CursosInscritosView.as_view(), name='cursos_inscrito'),
    path('tareas_pendiente/', TareasPendientesView.as_view(), name='tareas_pendiente'),
    path('entregar_tarea/', EntregarTareaView.as_view(), name='entregar_tarea'),
    path('editar_entrega/<int:id>', EntragaEditarEliminar.as_view(), name='editar_entrega'),
    path('lista_entregas/', EntregaListCreateView.as_view(), name='lista_entregas'),
    ###
    

]
