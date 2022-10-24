from django.contrib import admin
from django.urls import path
from .views import *

#Incluir aqui as urls das novas páginas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('cadastro/', CadastroView, name='indexcadastro'),
    path('cadastro/register/', RegisterView, name='register'),
    path('indicacoesNutricionais/', IndicacoesView, name='indicacoesNutricionais'),
    path('cadastro/nutritionist_register/', NutriRegisterView, name='nutritionistRegister'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('newRecipe/', NewRecipeView, name='novaReceita'),
    path('recipe/<int:id>/', ShowRecipeView, name='Receita'),
    path('feed/', FeedView, name='feed'),
    path('alimentos/', AlimentosView, name='alimentospage')
]
