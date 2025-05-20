import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny

from classroom.forms import CalificarEntregaForm, CursoForm, TareaForm
from classroom.models import Curso, Entrega, Tarea

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token(request):
    refresh = request.POST.get("refresh")
    Token = RefreshToken(refresh)
    return JsonResponse(
        {
            "token": {
                "refresh": str(Token),
                "access": str(Token.access_token),
            }
        }
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse(
            {
                "token": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                }
            }
        )
    else:
        return JsonResponse({"msg": "Credenciales incorrectas"})


@api_view(["POST"])
@permission_classes([AllowAny])
def registrar_usuario(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    rol = data.get("rol")
    user = User.objects.create_user(username=username, password=password, email=email)
    user.is_staff = rol == "profesor"
    user.rol = rol
    user.save()
    refresh = RefreshToken.for_user(user)
    return JsonResponse(
        {
            "token": {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        }
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def crear_curso(request):
    data = json.loads(request.body)
    form = CursoForm(data)
    if form.is_valid():
        curso = form.save(commit=False)
        curso.profesor = request.user
        print("curso", curso.id)
        curso.save()
        return JsonResponse({"curso": curso.id})
    else:
        return JsonResponse({"msg": "No es valido"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ver_entregas(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, curso__profesor=request.user)
    entregas = tarea.entregas.all()
    return JsonResponse({"tarea": tarea, "entregas": entregas})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def calificar_entrega(request, entrega_id):
    entrega = get_object_or_404(
        Entrega, id=entrega_id, tarea__curso__profesor=request.user
    )
    if request.method == "POST":
        form = CalificarEntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            return JsonResponse({"ver_entrega": entrega.id})
    else:
        form = CalificarEntregaForm(instance=entrega)
    return render(
        request, "classroom/calificar_entrega.html", {"form": form, "entrega": entrega}
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listar_cursos(request):
    cursos = list(Curso.objects.values())
    return JsonResponse({"cursos": cursos})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def crear_tarea(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, profesor=request.user)
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.curso = curso
            tarea.save()
            return JsonResponse({"tarea": tarea.id})
    else:
        form = TareaForm()
    return render(request, "classroom/crear_tarea.html", {"form": form, "curso": curso})
