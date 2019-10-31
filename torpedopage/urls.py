from django.urls import path
from . import views

from django.conf.urls import url
from torpedopage.views import RegistrarUsuario
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', LoginView.as_view(template_name='torpedopage/torpedo_index.html'), name='torpedo_index'),
    path('/nosotros', views.nosotros, name='nosotros'),
    path('/empezar', RegistrarUsuario.as_view(),name='empezar'),
    path('/user_page', views.base_user, name='user_page')

    
    
    
]

