from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from swepApp.models import *

class filtroTestes(StaticLiveServerTestCase):
    def setUp(self):
        self.browser =  webdriver.Chrome('e2e_tests/chromedriver.exe')
        self.browser.get("http://127.0.0.1:8000/feed/")
        self.usuario = User.objects.create_user(username='LULI')
        self.usuario.set_password('Pipoquinha146.')
        self.usuario.save()
        recipe = Recipe.objects.create(titulo ="bolo", ingredientes="Ovo", modoPreparo="bate", author=self.usuario, regiao="Nordeste")
        recipe.save()

    def tearDown(self):
        self.browser.close()

    def testeNordesteUrl(self):
        nordeste = self.browser.find_element(By.XPATH, '/html/body/div/div/a[3]')
        nordeste.click()

        certo="http://127.0.0.1:8000/feed/?q=Nordeste"
        self.assertEquals(self.browser.current_url, certo)
    def test_sul_url(self):
        sul = self.browser.find_element(By.XPATH, '/html/body/div/div/a[4]')
        sul.click()

        certo2="http://127.0.0.1:8000/feed/?q=Sul"
        self.assertEquals(self.browser.current_url, certo2)

    def test_sudeste_url(self):
        sudeste = self.browser.find_element(By.XPATH, '/html/body/div/div/a[5]')
        sudeste.click()

        certo3="http://127.0.0.1:8000/feed/?q=Sudeste"
        self.assertEquals(self.browser.current_url, certo3)

    def test_norte_url(self):
        Norte = self.browser.find_element(By.XPATH, '/html/body/div/div/a[2]')
        Norte.click()

        certo4="http://127.0.0.1:8000/feed/?q=Norte"
        self.assertEquals(self.browser.current_url, certo4)