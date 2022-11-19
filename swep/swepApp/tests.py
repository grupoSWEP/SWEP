from django.test import TestCase
from django.contrib.auth import get_user_model
from swepApp.models import *

class HomepageTests(TestCase):

    def setUp(self):
        self.nutritionist = Nutritionist.objects.create(email='vaquinha@malhada.com', username='vaquinha', first_name='vaquinha', last_name='malhada', crn='1234')
        self.nutritionist.save()

        self.regular = RegularUser.objects.create(email='nika@nikota.com', username='nika', first_name='nika', last_name='nikota')
        self.regular.save()

    def test_nutritionist_created(self):

        nutritionist = Nutritionist.objects.filter(email='vaquinha@malhada.com', username='vaquinha', first_name='vaquinha', last_name='malhada', crn='1234')

        self.assertTrue(nutritionist.exists())
        
        self.assertEqual(self.nutritionist.email, 'vaquinha@malhada.com')
        self.assertEqual(self.nutritionist.username, 'vaquinha')
        self.assertEqual(self.nutritionist.first_name, 'vaquinha')
        self.assertEqual(self.nutritionist.last_name, 'malhada')
        self.assertEqual(self.nutritionist.crn, '1234')
    
    def test_regular_created(self):

        regular = RegularUser.objects.filter(email='nika@nikota.com', username='nika', first_name='nika', last_name='nikota')

        self.assertTrue(regular.exists())
        self.assertEqual(self.regular.email, 'nika@nikota.com')
        self.assertEqual(self.regular.username, 'nika')
        self.assertEqual(self.regular.first_name, 'nika')
        self.assertEqual(self.regular.last_name, 'nikota')
