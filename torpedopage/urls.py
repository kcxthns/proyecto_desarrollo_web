from django.urls import path
from . import views

urlpatterns = [
    path('', views.torpedo_index, name='torpedo_index'),
    path('/nosotros', views.nosotros, name='nosotros'),
]