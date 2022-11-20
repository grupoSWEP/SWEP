from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required = True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    
    class Meta():
        
        model = RegularUser
    
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 
        ]


class NutriRegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required = True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required = True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    crn = forms.CharField(
        required = True,
        help_text='Enter CRN',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' CRN'}),
    )

    class Meta():
        
        model = Nutritionist
    
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'crn', 
        ]


class IndicacoesForm(forms.ModelForm):
    description2 = forms.CharField(
        required = True,
        help_text='Digite aqui...',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description2'}),
    )
    tipo = forms.CharField(
        max_length=200,
        required = True,
        help_text='Qual o tipo de informação? ',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tipo'}),
    )

    
    class Meta():
        
        model = Indicacoes
    
        fields = [
            'description2', 'tipo'
        ]
        
class NewRecipeForm(forms.ModelForm):
    regiao=forms.CharField(required=False)
    
    class Meta():
        
        model = Recipe
    
        fields = ['titulo', 'ingredientes', 'modoPreparo', 'regiao']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )