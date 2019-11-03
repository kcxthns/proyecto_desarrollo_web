from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import PreferenciasUsuario
from django import forms


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

class PreferenciaForm(forms.ModelForm):

    class Meta:
        model = PreferenciasUsuario
        fields = ('preferencia', 'idioma')


