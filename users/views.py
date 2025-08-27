from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):

    if(not request.user.is_authenticated):
        return redirect("forbidden")
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')

def signup_view(request):

    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username=request.POST.get('username')
        password= request.POST.get('password')
        User.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password
        )
        return redirect("login")
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def forbidden_view(request):
    return render(request, 'forbidden.html')
