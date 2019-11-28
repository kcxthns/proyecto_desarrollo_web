from django.contrib import admin
from .models import TextoPagina
from .models import ImagenPage
from .models import ImagenGaleria
from torpedopage.models import Apunte, ImagenLogo, ImagenSlider, Materia


admin.site.register(TextoPagina) #texto dinámico para la página
admin.site.register(ImagenLogo) #Imagenes Logo
admin.site.register(ImagenSlider)
admin.site.register(ImagenGaleria) #Imagenes de la galeria en template nosotros
admin.site.register(Apunte) #Torpedos
admin.site.register(Materia) #Materia para ser seleccionada al subir un archivo(torpedo)
