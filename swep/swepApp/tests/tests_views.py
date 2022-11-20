from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from swepApp.models import *
import json

class testView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='user')
        self.client = Client()
        Recipe.objects.create(
            author=self.user,
            id = '1'
            )

    def testFeedViews(self):

        response = self.client.get(reverse('feed'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed.html')

    def testRegisterGetViews(self):

        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def testNutriRegisterGetViews(self):

        response = self.client.get(reverse('nutritionistRegister'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nutriRegister.html')

    def testLoginGetViews(self):

        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def testAlimentosViews(self):

        response = self.client.get(reverse('alimentospage'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food.html')

    def testAlimentosViews(self):

        response = self.client.get(reverse('Receita', args=['1']))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showRecipe.html')
        