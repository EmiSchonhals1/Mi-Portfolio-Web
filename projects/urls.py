from django.urls import path
from .views import (
    index,
    portfolio,
    administrar_proyectos,
    cargar_documentos,
    aprendizaje,
    eliminar_documento,
)
from .views import eliminar_proyecto, lista_documentos, descargar_documento
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

def is_superuser(user):
    return user.is_superuser

admin.site.login = user_passes_test(lambda u: u.is_active and u.is_superuser)(admin.site.login)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('portfolio/', portfolio, name='portfolio'),
    path('eliminar-proyecto/<int:proyecto_id>/', eliminar_proyecto, name='eliminar_proyecto'),
    path('administrar-proyectos/', administrar_proyectos, name='administrar_proyectos'),
    path('cargar_documentos/', cargar_documentos, name='cargar_documentos'),
    path('aprendizaje/', aprendizaje, name='aprendizaje'),
    path("eliminar-documento/<int:documento_id>/", eliminar_documento, name="eliminar_documento"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)