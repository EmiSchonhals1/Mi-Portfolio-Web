from django.db import models
from django.contrib.auth.models import User
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    url = models.URLField(blank=True)
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class LearningFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='learning_files/')

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    

    
class Documento(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('pdf', 'PDF'),
        ('word', 'Word'),
        ('excel', 'Excel'),
        # Agrega más tipos según sea necesario
    ]

    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='documentos/')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)

    def __str__(self):
        return self.nombre


