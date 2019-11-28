from django.shortcuts import render
from .models import ImagenPage
from .models import ImagenGaleria

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from torpedopage.forms import ApunteForm, RegistroForm
from .forms import RegistroForm
from django.shortcuts import redirect


from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import LoginForm
from .forms import PreferenciaForm
from .models import PreferenciasUsuario
#from .models import Torpedo
#from .forms import TorpedoForm
from .models import Apunte
from django.utils import timezone
from torpedopage.models import TextoPagina
from django.contrib import messages
from django.core.paginator import Paginator





logo = ImagenPage.objects.filter(descripcion='logo torpedo')
#url nosotros
def nosotros(request):
    imagenGaleria = ImagenGaleria.objects.filter(nombre__icontains='galeria')
    return render(request, 'torpedopage/nosotros.html', {'logo': logo, 'imagenGaleria': imagenGaleria})
#url empezar
def empezar(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.save()
            return redirect('torpedo_index')
    else:
        form = RegistroForm()
    return render(request, 'torpedopage/empezar.html', {'logo': logo, 'form': form})
            

#def base_user(request):
    #usuario = request.user
    #torpedos = Apunte.objects.filter(autor=usuario)
    #return render(request, 'torpedopage/base_user.html', {'logo': logo, 'torpedos': torpedos}) 

#Inicio página Torpedo
def login(request):
    imagenSlider = ImagenPage.objects.filter(descripcion__icontains='slider')
    textoLogueado = TextoPagina.objects.filter(descripcion__icontains='texto_index_usuario_logueado')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                do_login(request, user)
                if user.is_staff:
                    return redirect('admin/')
                else:
                    return redirect('user_page')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos!!!')
            return redirect("/")
    return render(request, "torpedopage/torpedo_index.html", {'logo': logo, 'imagenSlider': imagenSlider, 'textoLogueado': textoLogueado})      

#url logout
def logout(request):
    do_logout(request)
    return redirect('/')

#Para la vista de preferencias (no implementada) 
"""
def preferencias(request):
    if request.method == "POST":
        form = PreferenciaForm(request.POST)
        if form.is_valid():
            PreferenciasUsuario = form.save(commit=False)
            PreferenciasUsuario.usuario = request.user
            PreferenciasUsuario.save()
            return redirect('user_page')
    else:
        form = PreferenciaForm()
    return render(request, 'torpedopage/preferencias.html', {'logo': logo, 'form': form})   
"""

#url agregar torpedo
def agregartorpedo(request):
    if request.method == 'POST':
        form = ApunteForm(request.POST, request.FILES)
        if form.is_valid():
            Apunte = form.save(commit=False)
            Apunte.autor = request.user
            Apunte.save()
            return redirect('user_page')
    else:
        form = ApunteForm()
    return render(request, 'torpedopage/agregartorpedo.html', {'logo': logo, 'form': form})

#url mis_aportes
def archivoTorpedo(request):
    usuario = request.user
    torpedos = Apunte.objects.filter(autor=usuario)
    
    if request.method == 'POST':
        autor = request.user
        id_torpedo = request.POST.get('id')
        torpedoBorrar = Apunte.objects.get(autor=autor, id=id_torpedo)
        torpedoBorrar.delete()

    paginador = Paginator(torpedos, 6)
    pagina = request.GET.get('page')
    torpedos = paginador.get_page(pagina)    
    return render(request, 'torpedopage/mis_aportes.html', {'logo': logo, 'torpedos': torpedos, })

#url buscar_torpedo
def buscarTorpedo(request):
    context = {'logo':logo}
    if request.method == "GET":
        criterio_busqueda = request.GET.get("q")
        submitbutton = request.GET.get("submit")
        if criterio_busqueda is not None:
            torpedos_encontrados = Apunte.objects.filter(titulo__icontains=criterio_busqueda)
            paginador = Paginator(torpedos_encontrados, 6)
            pagina = request.GET.get('page')
            torpedos_encontrados = paginador.get_page(pagina)
            context = {'logo':logo, 'torpedos_encontrados':torpedos_encontrados, 'submitbutton': submitbutton}
            
            #Permite continuear con la paginación
            parametros = request.GET.copy() #Copia del GET
            if 'page' in parametros:
                del parametros['page'] #borra parametro page
            context['parametros'] = parametros

            return render(request, 'torpedopage/buscar_torpedo.html', context)
    return render(request, 'torpedopage/buscar_torpedo.html', context)
     
def editarTorpedo(request, torpedo_id):
    torpedo = Apunte.objects.get(id=torpedo_id)
    form = ApunteForm(instance=torpedo)

    if request.method == 'POST':
        form = ApunteForm(request.POST, instance=torpedo)
        if form.is_valid:
            torpedo = form.save(commit=False)
            torpedo.save()
            return redirect('user_page')
    return render(request, 'torpedopage/editar_torpedo.html', {'logo': logo, 'form':form})

def passwordResetCompleto(request):
    return render(request, 'registration/password_reset_complete_custom.html', {'logo':logo})

def logoPagina(request):
    return render(request, 'torpedopage/logo.html', {'logo':logo})
    
    
