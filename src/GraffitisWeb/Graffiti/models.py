# from django.db import models
from django.db import models
from djongo.models import JSONField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django import forms

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        if not username:
            raise ValueError('El usuario debe tener un username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    # Campos necesarios para la clase
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Campos propios
    descripcion = models.CharField(max_length=50)
    usuario_id = models.AutoField(primary_key=True)
    seguidores = models.ManyToManyField('self', null=True, blank=True, related_name='reverse_seguidores', symmetrical=False)
    seguidos = models.ManyToManyField('self', null=True, blank=True, related_name='reverse_seguidos', symmetrical=False)


    USERNAME_FIELD = 'email' # Campo requerido para el login
    REQUIRED_FIELDS = ['username']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


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