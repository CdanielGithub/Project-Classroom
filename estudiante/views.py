from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now
from classroom.models import Entrega, Tarea, Curso

from .serializers import EntregaSerializer, TareaSerializer, CursoSerializer



# Create your views here.


class EntregaListCreateView(generics.ListAPIView):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class TareaListCreateView(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class CursoListCreateView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


##

class EntregarTareaView(generics.CreateAPIView):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class EntragaEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    lookup_field ='id'


class TareasPendientesView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        user = request.user

        cursos = Curso.objects.filter(estudiantes=user)

        tareas = Tarea.objects.filter(curso__in=cursos)

        entregadas = Entrega.objects.filter(estudiante=user).values_list('tarea_id', flat=True)

        pendientes = tareas.exclude(id__in=entregadas).filter(fecha_entrega__gte=now())

        tareas_data = [
            {
                "id": tarea.id,
                "titulo": tarea.titulo,
                "descripcion": tarea.descripcion,
                "curso": tarea.curso.nombre,
                "fecha_entrega": tarea.fecha_entrega
            }
            for tarea in pendientes
        ]

        return Response(tareas_data)
