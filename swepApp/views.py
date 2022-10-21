from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, IndicacoesForm, LoginForm, NewRecipeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here. - Criar as Views de cada página.
def IndexView(request):
    return render(request, 'landing.html')

def CadastroView(request):
    return render(request, 'landingCad.html')

def RegisterView(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'register.html', context)
    
    return render(request, 'register.html', {})

@login_required
def IndicacoesView(request):
    if request.method == 'GET':
        form  = IndicacoesForm()
        context = {'form': form}
        return render(request, 'indicacoes.html', context)
    
    if request.method == 'POST':
        form  = IndicacoesForm(request.POST)
        
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            description2 = form.cleaned_data.get('description2')
            messages.success(request, 'Indicação nutricional postada')
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'indicacoes.html', context)
    
    return render(request, 'indicacoes.html', {})

@login_required
def NewRecipeView(request):
    if request.method == 'GET':
        form  = NewRecipeForm()
        context = {'form': form}
        return render(request, 'receitas.html', context)
    
    if request.method == 'POST':
        form  = NewRecipeForm(request.POST)
        
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'receitas.html', context)
    
    return render(request, 'receitas.html', {})

def LoginView(request):
    if request.method == 'GET':
        form  = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    
    if request.method == 'POST':
        form  = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'login.html', context)
    
    return render(request, 'login.html', {})

def LogoutView(request):
    logout(request)
    return redirect('index')
