from django.contrib import admin
from .models import Usuario, Publicacion, Comentario, Graffiti

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Graffiti)
admin.site.register(Publicacion)