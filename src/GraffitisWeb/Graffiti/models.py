# from django.db import models
from django.db import models
from djongo.models import JSONField
# from django import forms

# Create your models here.
class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    psw = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    seguidores = models.ManyToManyField('self', null=True, blank=True, related_name='reverse_seguidores', symmetrical=False)
    seguidos = models.ManyToManyField('self', null=True, blank=True, related_name='reverse_seguidos', symmetrical=False)

    def __str__(self):
        return str(self.usuario_id)


class Graffiti(models.Model):
    graffiti_id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_autor')
    publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE, related_name='graffitis')

    imagen = models.URLField(null=False)
    estado = models.CharField(max_length=30) # usar enumerado
    fechaCaptura = models.DateField(null=False)
    
    def __str__(self):
        return self.graffiti_id

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_autor')
    publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE, related_name='comentarios')

    texto = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return str(self.comentario_id)

class Publicacion(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='publicaciones')
    likes = models.ManyToManyField(Usuario, related_name='likes')

    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=500, blank=True)
    localizacion = models.CharField(max_length=50, null=False)
    tematica = JSONField()
    
    def __str__(self):
        return str(self.publicacion_id)






# =========================================================================================================================
# class Usuario(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # Extender la clase User del modulo Auth 
#     descripcion = models.CharField(max_length=500, blank=True)

#     listaSeguidores = models.ArrayReferenceField(to='self', null=True,blank=True, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_seguidores')
#     listaSeguidos = models.ArrayReferenceField(to='self', null=True, blank=True, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_seguidos')
#     # listaGraffiti = models.ArrayReferenceField(to='GraffitiAbstract', on_delete=models.CASCADE)
#     listaPublicaciones = models.ArrayReferenceField(to='Publicacion', null=True, blank=True, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user.username


# class GraffitiAbstract(models.Model):
#     imagen = models.URLField(null=False)
#     estado = models.CharField(max_length=30) # usar enumerado
#     fechaCaptura = models.DateField(null=False)
#     autor = models.PositiveIntegerField(null=False)

#     def __str__(self):
#         return f'[{self.imagen}, {self.estado}, {self.fechaCaptura}]'    
    
#     class Meta:
#         abstract = True

    
# class ComentarioAbstract(models.Model):
#     texto = models.CharField(max_length=200, null=False)
#     # Una solucion para los autores seria colocar un simple campo sin relacione
#     # y ocuparse en el codigo de meter el id del usuario que ha hecho el comentario
#     autor = models.PositiveIntegerField(null=False)

#     def __str__(self):
#         return self.texto

#     class Meta:
#         abstract = True

# # class Comentario(ComentarioAbstract):
# #     autor = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s_s')

# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args,**kwargs)


# class Publicacion(models.Model):
#     id = models.AutoField(primary_key=True)
    
#     titulo = models.CharField(max_length=100, null=False)
#     descripcion = models.CharField(max_length=500, blank=True)
#     localizacion = models.CharField(max_length=50, null=False)
#     # tematica = models.JSONField()
#     autor = models.CharField(max_length=50)
#     creador = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_creador') 
#     listaGraffiti = models.ArrayField(model_container=GraffitiAbstract)
#     listaComentario = models.ArrayField(model_container=ComentarioAbstract)
#     meGusta = models.ArrayReferenceField(to=Usuario, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_meGusta') # cambiar por manyToMany

#     def __str__(self):
#         return f'{self.id} {self.titulo}'



    



    




