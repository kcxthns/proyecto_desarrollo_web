from django.db import models
from django.utils import timezone
from torpedopage.FileFieldRestriccion import ContentTypeRestrictedFileField

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
    nombre = models.CharField(primary_key=True, max_length=200, help_text="Debe contener la palabra galeria")
    descripcion = models.CharField(max_length=250, help_text="Descripción que aparecerá al pie de la foto en la galería")
    imagen = models.ImageField(upload_to='media/galeria')



class PreferenciasUsuario(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    preferencia = models.CharField(max_length=100)
    idioma = models.CharField(max_length=50)
    
    def __str__(self):
        return self.preferencia


#class Torpedo(models.Model):
    #autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)  
    #titulo = models.CharField(max_length=100) 
    #fecha_creacion = models.DateTimeField(
        #default=timezone.now)
    #fecha_publicacion = models.DateTimeField(blank=True, null=True) 
    #materia = models.CharField(max_length=200)
    #like = models.IntegerField(default=0, blank=True, null=True) 
    #media = models.FileField(upload_to='media/torpedos')

    #def fecha(self):
        #self.fecha_publicacion = timezone.now()
        #self.save()

    #def __str__(self):
        #return self.materia

class Materia(models.Model):
    materia = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.materia

class Apunte(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    #documento = models.FileField(upload_to='media/documents')
    documento = ContentTypeRestrictedFileField(
        upload_to='media/documents',
        content_types=['application/pdf', 
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                        'application/msword',
                        'text/plain'],
        max_upload_size=2621440
        )

    def __str__(self):
        return self.titulo




