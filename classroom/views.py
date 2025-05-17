from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Tarea, Entrega
from .forms import CursoForm, TareaForm, CalificarEntregaForm


@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.profesor = request.user
            curso.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'classroom/crear_curso.html', {'form': form})


@login_required
def listar_cursos(request):
    cursos = Curso.objects.filter(profesor=request.user)
    return render(request, 'classroom/listar_cursos.html', {'cursos': cursos})


@login_required
def crear_tarea(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, profesor=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.curso = curso
            tarea.save()
            return redirect('detalle_curso', curso_id=curso.id)
    else:
        form = TareaForm()
    return render(request, 'classroom/crear_tarea.html', {'form': form, 'curso': curso})


@login_required
def ver_entregas(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, curso__profesor=request.user)
    entregas = tarea.entregas.all()
    return render(request, 'classroom/ver_entregas.html', {'tarea': tarea, 'entregas': entregas})


@login_required
def calificar_entrega(request, entrega_id):
    entrega = get_object_or_404(Entrega, id=entrega_id, tarea__curso__profesor=request.user)
    if request.method == 'POST':
        form = CalificarEntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            return redirect('ver_entregas', tarea_id=entrega.tarea.id)
    else:
        form = CalificarEntregaForm(instance=entrega)
    return render(request, 'classroom/calificar_entrega.html', {'form': form, 'entrega': entrega})



@login_required
def calificar_entrega(request, entrega_id):
    entrega = get_object_or_404(Entrega, id=entrega_id, tarea__curso__profesor=request.user)
    if request.method == 'POST':
        form = CalificarEntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            return redirect('ver_entregas', tarea_id=entrega.tarea.id)
    else:
        form = CalificarEntregaForm(instance=entrega)
    return render(request, 'classroom/calificar_entrega.html', {'form': form, 'entrega': entrega})


