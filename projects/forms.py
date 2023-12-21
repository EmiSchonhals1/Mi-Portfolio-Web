from django import forms
from .models import Project, Documento

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario
        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nombre', 'archivo', 'tipo_documento']