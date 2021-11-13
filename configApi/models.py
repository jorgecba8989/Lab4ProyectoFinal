from django.db import models
from django.db.models.fields import DateField
from rest_framework import serializers
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'



class Video(models.Model):
    cantante = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.cantante}"

    class Meta:
        verbose_name='Video'
        verbose_name_plural='Videos'


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    clave =  models.IntegerField(default=0)
    clave2 =  models.IntegerField(default=0)
    correo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
    
    def validate(self, attrs):
        if attrs['clave'] != attrs['clave2']:
            raise serializers.ValidationError({"clave": "Las claves no coinciden.."})
        return attrs

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'


class Comentario(models.Model):
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField(default=DateField)
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comentarios')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='comentarios')

    class Meta:
        verbose_name='Comentario'
        verbose_name_plural='Comentarios'



class Like(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='likes' )
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='likes')

    class Meta:
        verbose_name='Like'
        verbose_name_plural='Likes'



class Listado(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Listado'
        verbose_name_plural='Listados'



class ListadoVideo(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name='ListadoVideo'
        verbose_name_plural='ListadosVideos'