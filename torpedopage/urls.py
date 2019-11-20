from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', views.login,  name='torpedo_index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('empezar', views.empezar ,name='empezar'),
    path('user_page', views.base_user, name='user_page'),
    path('logout', views.logout),
    path('preferencias', views.preferencias, name='preferencias'),
    path('agregartorpedo', views.agregartorpedo, name='agregartorpedo'),
    path('mis_aportes', views.archivoTorpedo, name='mis_aportes'),
    path('buscar_torpedo', views.buscarTorpedo, name='buscar_torpedo'),

    
    
    
]

