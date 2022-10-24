from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here. - Criar as Views de cada página.

def nutriOnly(function):
    def wrapper(request):
        if request.user.is_authenticated:
            a = Nutritionist.objects.get(id = request.user.id)
            if a!=None:
                return function(request)
    return wrapper

def IndexView(request):
    return render(request, 'landing.html')

def CadastroView(request):
    return render(request, 'landingCad.html')

def FeedView(request):
    return render(request, 'feed.html')

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

def NutriRegisterView(request):
    if request.method == 'GET':
        form  = NutriRegisterForm()
        context = {'form': form}
        return render(request, 'nutriRegister.html', context)
    
    if request.method == 'POST':
        form  = NutriRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'nutriRegister.html', context)
    
    return render(request, 'nutriRegister.html', {})

@nutriOnly
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
            return redirect('feed')
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
            return redirect('feed')
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
            return redirect('feed')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'login.html', context)
    
    return render(request, 'login.html', {})

def LogoutView(request):
    logout(request)
    return redirect('index')

def ShowRecipeView(request, id):
    recipe = Recipe.objects.get(id=id)
    context = { 'recipe':recipe }
    return render(request, 'showRecipe.html', context)
@csrf_exempt
def AlimentosView(request):
    if request.method=='POST':
        alim=request.POST.getlist('alimentos')
        Alimentos.objects.create(alimentos=alim)
        return redirect('index')
    return render (request, 'food.html')
        

def FeedView(request):
    posts = Recipe.objects.all().order_by('-id')
    return render(request, 'feed.html',  {'posts': posts})
    

   