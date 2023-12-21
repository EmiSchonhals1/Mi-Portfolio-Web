# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Skill, LearningFile, Documento
from .forms import ProjectForm, DocumentoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin





def index(request):
    return render(request, 'index.html')

def pre_home(request):
    return render(request, 'pre_home.html')

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def about_me(request):
    skills = Skill.objects.all()
    return render(request, 'about_me.html', {'skills': skills})

def learning(request):
    learning_files = LearningFile.objects.all()
    return render(request, 'learning.html', {'learning_files': learning_files})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

@login_required
def administrar_proyectos(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password != '100604':
            return HttpResponseForbidden("Usted no puede acceder a esta sección.")
        
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto agregado exitosamente.')
            return redirect('administrar_proyectos')
    else:
        form = ProjectForm()

    projects = Project.objects.all()
    
    if request.method == 'GET' and 'eliminar_proyecto' in request.GET:
        proyecto_id = request.GET['eliminar_proyecto']
        project = Project.objects.get(pk=proyecto_id)
        project.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
        return redirect('administrar_proyectos')

    return render(request, 'administrar_proyectos.html', {'projects': projects, 'form': form})

@login_required
def eliminar_proyecto(request, proyecto_id):
    try:
        project = Project.objects.get(pk=proyecto_id)
        project.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
    except Project.DoesNotExist:
        messages.error(request, 'El proyecto no existe.')

    return redirect('administrar_proyectos')

# Definir la contraseña requerida
CONTRASENA_REQUERIDA = "100604"

@login_required
def cargar_documentos(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')

        # Verificar la contraseña
        if password == '100604':
            form = DocumentoForm(request.POST, request.FILES)
            if form.is_valid():
                # Guardar el tipo de documento correctamente
                documento = form.save(commit=False)
                documento.usuario = request.user
                documento.save()
                messages.success(request, 'Documento cargado exitosamente.')
                return redirect('cargar_documentos')
        else:
            messages.error(request, 'Contraseña incorrecta. No se pudo cargar el documento.')
    else:
        form = DocumentoForm()

    documentos = Documento.objects.all()

    return render(request, 'cargar_documentos.html', {'form': form, 'documentos': documentos})


# Decorador para verificar la contraseña
def verificar_contrasena(view_func):
    def _wrapped_view(request, *args, **kwargs):
        contrasena_ingresada = request.POST.get("contrasena", "")  # Asegúrate de que "contrasena" es el nombre correcto del campo en tu formulario
        if contrasena_ingresada != CONTRASENA_REQUERIDA:
            return HttpResponseForbidden("Acceso denegado. Contraseña incorrecta.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Vista para eliminar documentos con verificación de contraseña
#@verificar_contrasena
@login_required
def eliminar_documento(request, documento_id):
    documento = Documento.objects.get(id=documento_id)

    # Verificar la contraseña
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == '100604':
            # Contraseña correcta, eliminar el documento
            documento.delete()
            messages.success(request, 'Documento eliminado exitosamente.')
            return redirect('cargar_documentos')
        else:
            # Contraseña incorrecta, mostrar mensaje de error
            messages.error(request, 'Contraseña incorrecta. No se pudo eliminar el documento.')

    return render(request, 'eliminar_documento.html', {'documento': documento})

def aprendizaje(request):
    documentos = Documento.objects.all()  # Obtén todos los documentos, no solo los del usuario autenticado

    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.save()
            return redirect('aprendizaje')
    else:
        form = DocumentoForm()

    return render(request, 'aprendizaje.html', {'documentos': documentos, 'form': form})




def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'lista_documentos.html', {'documentos': documentos})

def descargar_documento(request, documento_id):
    documento = Documento.objects.get(id=documento_id)
    response = HttpResponse(documento.archivo, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={documento.archivo.name}'
    return response

