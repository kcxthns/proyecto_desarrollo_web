from django.shortcuts import render
from .models import ImagenPage
from .models import ImagenGaleria

def torpedo_index(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenSlider = ImagenPage.objects.filter(descripcion__icontains='slider')
    return render(request, 'torpedopage/torpedo_index.html', {'logo': logo, 'imagenSlider': imagenSlider})

def nosotros(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenGaleria = ImagenGaleria.objects.filter(nombre__icontains='galeria')
    return render(request, 'torpedopage/nosotros.html', {'logo': logo, 'imagenGaleria': imagenGaleria})
