from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Exceptions

from django.db.utils import IntegrityError

# models

from django.contrib.auth.models import User
from users.models import Profile

def update_profile(request):
    return render(request, 'users/update_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['pass']
        passwd_confirmation= request.POST['pass_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd) 
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'User already exists'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request, 'users/signup.html')