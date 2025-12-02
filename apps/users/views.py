from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            error = "Credenciales inválidas"
            return render(request, 'users/login.html', {'error': error})
        
    else:
        return render(request, 'users/login.html', {'next': request.GET.get('next', '')})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        
        else:
            return render(request, 'users/register.html', {'error': 'Las contraseñas no coinciden'})
        
    return render(request, 'users/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')