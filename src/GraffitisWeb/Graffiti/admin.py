from django.contrib import admin
from .models import Usuario, Graffiti, Comentario, Publicacion, PublicacionBien

# Register your models here.
admin.site.register(Usuario)
admin.site.register(PublicacionBien)
