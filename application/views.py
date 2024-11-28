from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')
        
        messages.success(request, 'Chyba pri prihlasovani')
        return redirect('login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
