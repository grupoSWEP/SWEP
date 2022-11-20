from django.test import TestCase
from django.contrib.auth import get_user_model
from swepApp.forms import *

class testRegister(TestCase):

    def testRegisterFormValid(self):
        form = RegisterForm(data={
            "username":"vaquinha",
            "email":"vaquinha@malhada.com",
            "first_name":"vaquinha",
            "last_name":"malhada",
            "password1":"Bezerrinhos123",
            "password2":"Bezerrinhos123"})
        
        self.assertTrue(form.is_valid())

    def testRegisterFormInvalid(self):
        form = RegisterForm(data={
            "username":"vaquinha",
            "email":"vaquinha@malhada.com",
            "first_name":"vaquinha",
            "last_name":"malhada",
            "password1":"Bezerrinhos123",
            "password2":"Cabritinhos123"})
        
        self.assertFalse(form.is_valid())

class testNutriRegister(TestCase):

    def testNutriRegisterFormValid(self):
        form = NutriRegisterForm(data={
            "username":"nika",
            "email":"nika@nikota.com",
            "first_name":"nika",
            "last_name":"nikota",
            "crn":"12345",
            "password1":"Cachorro123",
            "password2":"Cachorro123"})

        self.assertTrue(form.is_valid())

    def testNutriRegisterFormInvalid(self):
        form = NutriRegisterForm(data={
            "username":"nika",
            "email":"nika@nikota.com",
            "first_name":"nika",
            "last_name":"nikota",
            "crn":"12345",
            "password1":"Cachorro123",
            "password2":"Cachorrinho123"})

        self.assertFalse(form.is_valid())        