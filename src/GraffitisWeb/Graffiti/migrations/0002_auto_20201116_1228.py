# Generated by Django 3.0.5 on 2020-11-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graffiti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='seguidores',
        ),
        migrations.AddField(
            model_name='usuario',
            name='seguidores',
            field=models.ManyToManyField(blank=True, null=True, related_name='_usuario_seguidores_+', to='Graffiti.Usuario'),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='seguidos',
        ),
        migrations.AddField(
            model_name='usuario',
            name='seguidos',
            field=models.ManyToManyField(blank=True, null=True, related_name='_usuario_seguidos_+', to='Graffiti.Usuario'),
        ),
    ]