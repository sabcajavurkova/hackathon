from django.shortcuts import render


def index():
     return render(request, 'homepage.html')