from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('pre-home/', include('projects.urls')),  
    path('home/', include('projects.urls')),
    path('about-me/', include('projects.urls')),
    path('learning/', include('projects.urls')),
    path('portfolio/', include('projects.urls')),
    path('aprendizaje/', include('projects.urls')),
    path('cargar_documentos/', include('projects.urls')),
]


