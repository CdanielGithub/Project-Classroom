from django.urls import path
from .views import EntregaListCreateView, EntregarTareaView,CursoListCreateView, TareaListCreateView, TareasPendientesView, EntragaEditarEliminar, CursosInscritosView
#, MisEntregasView
urlpatterns = [
    path('entregas/', EntregaListCreateView.as_view(), name='entregas'),
    path('entregar/', EntregarTareaView.as_view(), name='entregar-tarea'),
    
   #path('cursos/', CursoListCreateView.as_view(), name='cursos'),
   #path('tareas/', TareaListCreateView.as_view(), name='tareas'),
   path('tareas-pendientes/', TareasPendientesView.as_view(), name='tareas-pendientes'),
   path('editar-entrega/<int:id>', EntragaEditarEliminar.as_view(), name='editar-entrega'),
   path('cursos_inscrito/', CursosInscritosView.as_view(), name='cursos_inscrito'),


]
