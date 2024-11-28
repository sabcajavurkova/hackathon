from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterUserForm
from .models import Student, Teacher

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        
        return redirect('/prihlaseni')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mac_address = form.cleaned_data['mac_address']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            if role == 'Zak':
                Student.objects.create(user=user, first_name=first_name, last_name=last_name, mac_address=mac_address)
            elif role == 'Ucitel':
                Teacher.objects.create(user=user, first_name=first_name, last_name=last_name, mac_address=mac_address)
            
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})
