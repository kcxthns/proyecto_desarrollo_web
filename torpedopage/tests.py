from django.test import TestCase
from django.test import Client
from .forms import *

class Pruebas(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test',
        password='passtest12345',
        is_superuser=False,
        first_name='usuariotest',
        last_name='testusuario',
        email='emailtest@email.com')


    #def test_fields(self):
        #user = User.objects.get(id=1)
        #fields = user._meta.fields
        #print(fields)



    def test_username(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'nombre de usuario')
    
    def test_password(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'contraseña')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 150)

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)
    
    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 150)