from django.test import TestCase
from django.contrib.auth import get_user_model
from swepApp.models import *

class testeTests(TestCase):

    def setUp(self):
        self.nutritionist = Nutritionist.objects.create(
            email='vaquinha@malhada.com',
            username='vaquinha', 
            first_name='vaquinha', 
            last_name='malhada', 
            crn='1234')
        self.nutritionist.save()

        self.regular = RegularUser.objects.create(
            email='nika@nikota.com', 
            username='nika', 
            first_name='nika', 
            last_name='nikota')
        self.regular.save()

    def tearDown(self):
        self.regular.delete()
        self.nutritionist.delete()

    def test_nutritionist_created(self):

        nutritionist = Nutritionist.objects.filter(
            email='vaquinha@malhada.com', 
            username='vaquinha', 
            first_name='vaquinha', 
            last_name='malhada', 
            crn='1234')

        self.assertTrue(nutritionist.exists())
        
        self.assertEqual(self.nutritionist.email, 'vaquinha@malhada.com')
        self.assertEqual(self.nutritionist.username, 'vaquinha')
        self.assertEqual(self.nutritionist.first_name, 'vaquinha')
        self.assertEqual(self.nutritionist.last_name, 'malhada')
        self.assertEqual(self.nutritionist.crn, '1234')
    
    def test_regular_created(self):

        regular = RegularUser.objects.filter(
            email='nika@nikota.com', 
            username='nika', 
            first_name='nika', 
            last_name='nikota')

        self.assertTrue(regular.exists())
        self.assertEqual(self.regular.email, 'nika@nikota.com')
        self.assertEqual(self.regular.username, 'nika')
        self.assertEqual(self.regular.first_name, 'nika')
        self.assertEqual(self.regular.last_name, 'nikota')

class testRecipe(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.save()

        self.recipe = Recipe.objects.create(
            titulo='chocolate', 
            ingredientes='cacau', 
            modoPreparo='seinao', 
            author=self.user)
        self.recipe.save()

    def tearDown(self):
        self.recipe.delete()

    def testRightRecipe(self):
        self.assertEqual(self.recipe.titulo,'chocolate')
        self.assertEqual(self.recipe.ingredientes,'cacau')
        self.assertEqual(self.recipe.modoPreparo,'seinao')
        self.assertEqual(self.recipe.author,self.user)

class testindicacao(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.user.save()

        self.indicacoes = Indicacoes.objects.create(
            description2='indicacao',
            tipo='tipo',
            author=self.user,)
        self.indicacoes.save()

    def tearDown(self):
        self.user.delete()

    def testRightIndicacao(self):
        self.assertEqual(self.indicacoes.description2,'indicacao')
        self.assertEqual(self.indicacoes.tipo,'tipo')
        self.assertEqual(self.indicacoes.author, self.user)
