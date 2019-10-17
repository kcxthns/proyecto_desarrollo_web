from django.shortcuts import render
from .models import ImagenPage

def torpedo_index(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenSlider = ImagenPage.objects.filter(descripcion__contains='slider')
    imagenGaleria = ImagenPage.objects.filter(descripcion__contains='galeria')
    return render(request, 'torpedopage/torpedo_index.html', {'logo': logo, 'imagenSlider': imagenSlider,
    'imagenGaleria': imagenGaleria})

def nosotros(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenGaleria = ImagenPage.objects.filter(descripcion__contains='galeria')
    return render(request, 'torpedopage/nosotros.html', {'logo': logo, 'imagenGaleria': imagenGaleria})
