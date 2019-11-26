from django.urls import include, path, reverse_lazy
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


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

    #Cambiar Contraseña
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_d.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'),
        name='password_change'),

    #Reset Contraseña    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done_custom.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm_custom.html',
        success_url=reverse_lazy('reset_completo')), 
        name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_formu.html'),
        name='password_reset'),
    
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        #template_name='registration/password_reset_complete_custom.html'), 
        #name='password_reset_complete'),

    path('cambio_exitoso', views.passwordResetCompleto, name='reset_completo'),

    #path('logo/', views.logoPagina, name='logo')
]

