# from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from djongo import models
from django import forms

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Extender la clase User del modulo Auth
    
    descripcion = models.CharField(max_length=500, blank=True)
    # listaSeguidores = models.ArrayReferenceField(to='self', on_delete=models.CASCADE, related_name='Usuarios_seguidores', default=[])
    # listaSeguidos = models.ArrayReferenceField(to='self', on_delete=models.CASCADE, related_name='Usuarios_seguidos', default=[])
    # listaGraffiti = models.ArrayReferenceField(to='Graffiti', on_delete=models.CASCADE)
    # listaPublicaciones = models.ArrayReferenceField(to='Publicacion', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

# class UsuarioForm(forms.ModelForm):
#     model = Usuario
#     fields = (
#         'user', 'descripcion'
#     )

# class GraffitiAbstracto(models.Model):
#     class Meta:
#             abstract = True

class Graffiti(models.Model):
    imagen = models.URLField(null=False)
    estado = models.CharField(max_length=30) # usar enumerado
    fechaCaptura = models.DateField(null=False)
    
    
    class Meta:
        abstract = True

class GraffitiBien(Graffiti):
    autor = models.ForeignKey(Usuario, null= False, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s_s')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    

# class GraffitiForm(forms.ModelForm):
#     class Meta:
#         model = Graffiti
#         fields = (
#             'imagen','estado', 'fechaCaptura', 'autor'
#         )

    
class Comentario(models.Model):
    texto = models.CharField(max_length=200, null=False)

    class Meta:
        abstract = True

# class ComentarioForm(forms.ModelForm):
#     model = Comentario
#     fields = (
#         'texto', 'autor'
#     )

class ComentarioBien(Comentario):
    autor = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s_s')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)


class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=500, blank=True)
    localizacion = models.CharField(max_length=50, null=False)
    # tematica = models.JSONField()
    autor = models.CharField(max_length=50)
    
    
    # listaComentario = models.ArrayField(model_container=Comentario)
    # meGusta = models.ArrayReferenceField(to=Usuario, on_delete=models.CASCADE)
    class Meta:
        abstract = True
# class PublicacionForm(forms.ModelForm):
#     class Meta:
#         model = Publicacion
#         fields = (
#             'id', 'creador', 'titulo', 'descripcion', 'localizacion', 'tematica', 'autor'
#         )
class PublicacionBien(Publicacion):
    creador = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE) 
    listaGraffiti = models.ArrayField(model_container=Graffiti, null = False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    



    




