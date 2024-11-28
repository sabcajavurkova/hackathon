from django.shortcuts import render
from .models import Report

def report(request):
    return render(request, 'report-index.html', {})

def zobrazit(request):
    reports = Report.objects.all()
    return render(request, 'zobrazit-index.html', {'reports': reports})
