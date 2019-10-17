from django.contrib import admin
from .models import TextoPagina
from .models import ImagenPage
from .models import ImagenGaleria

admin.site.register(TextoPagina)
admin.site.register(ImagenPage)
admin.site.register(ImagenGaleria)
