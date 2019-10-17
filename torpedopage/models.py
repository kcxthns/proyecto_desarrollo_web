from django.db import models

class TextoPagina(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.descripcion

class ImagenPage(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.descripcion

class ImagenGaleria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=200)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='media/galeria')