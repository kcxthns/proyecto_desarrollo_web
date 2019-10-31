from django.shortcuts import render
from .models import ImagenPage
from .models import ImagenGaleria

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from torpedopage.forms import RegistroForm




def torpedo_index(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenSlider = ImagenPage.objects.filter(descripcion__icontains='slider')
    return render(request, 'torpedopage/torpedo_index.html', {'logo': logo, 'imagenSlider': imagenSlider})

def nosotros(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    imagenGaleria = ImagenGaleria.objects.filter(nombre__icontains='galeria')
    return render(request, 'torpedopage/nosotros.html', {'logo': logo, 'imagenGaleria': imagenGaleria})

def empezar(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    return render(request, 'torpedopage/empezar.html', {'logo': logo})

def base_user(request):
    logo = ImagenPage.objects.filter(descripcion='logo torpedo')
    return render(request, 'torpedopage/base_user.html', {'logo': logo})    


     
class RegistrarUsuario(CreateView):
    model = User
    template_name = "torpedopage/empezar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('torpedo_index')
 
    
    
