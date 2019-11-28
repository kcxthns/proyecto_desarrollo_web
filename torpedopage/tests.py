from django.test import TestCase
from django.test import Client
from .forms import *

#class Setup_Class(TestCase):
    #def setUp(self):
        #self.user = User.objects.create(username='test',
        #password='passtest12345',
        #first_name='usuariotest',
        #last_name='testusuario',
        #email='emailtest@email.com')

class Pruebas(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='test',
        password='passtest12345',
        first_name='usuariotest',
        last_name='testusuario',
        email='emailtest@email.com')


    #def test_fields(self):
        #user = User.objects.get(id=1)
        #fields = user._meta.fields
        #print(fields)

    def test_form_registro(self):
        #user = User.objects.get(id=1)
        form = RegistroForm(data={
        'username': "test",
        'password':"passtest12345",
        'first_name':"usuariotest",
        'last_name':"testusuario",
        'email':"emailtest@email.com"
        })
        self.assertTrue(form.is_valid)