from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import PreferenciasUsuario
from django import forms
from torpedopage.models import Apunte
#from .models import Torpedo
from torpedopage.models import Apunte

#formulario de registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
    labels = {
        'username': 'Nombre de usuario',
        'first_name': 'Nombre Completo',
        'last_name': 'Apellido',
        'email': 'Email',
    }  
#formulario de login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'userame',
            'password',
        ]
    labels = {
        'username': 'username',
        'password' : 'password'
    }
#Formulario de preferencias (no usado)
class PreferenciaForm(forms.ModelForm):

    class Meta:
        model = PreferenciasUsuario
        fields = ('preferencia', 'idioma')
#Formulario para subir Torpedo
class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ['titulo', 'descripcion', 'materia', 'documento', ]
        labels = {
            'titulo':'Título',
            'descripcion':'Descripción',
            'materia':'Materia',
            'documento':'Archivo'
        }


