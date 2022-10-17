from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserSwep(AbstractUser):
    idade = models.IntegerField(null=True, blank=True)


class Recipe(models.Model):
    titulo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=500)
    modoPreparo = models.TextField()
    author = models.ForeignKey(UserSwep, on_delete=models.CASCADE)
    class RegiaoEnum(models.TextChoices):
        NORTE = 'NO', ('Norte')
        NORDESTE = 'NE', ('Nordeste')
        CENTROOESTE = 'CO', ('Centro-Oeste')
        SUL = 'SU', ('Sul')
        SUDESTE = 'SE', ('Sudeste')
    regiao = models.CharField(
        max_length=2,
        choices= RegiaoEnum.choices, 
        null=True)

    def str(self):
        return self.titulo

class Indicacoes(models.Model):
    description2 = models.TextField()
    tipo = models.CharField(max_length=50)
    author = models.ForeignKey(UserSwep, on_delete=models.CASCADE)

    def str(self):
        return self.decription2
