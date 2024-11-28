from django.shortcuts import render
from .models import Report

def report(request):
    return render(request, 'report-index.html', {})

def zobrazit(request):
    
    if request.method == 'POST':
        search_query = request.POST['search_query']
        reports = Report.objects.filter(address__contains=search_query).order_by('date')
        return render(request, 'zobrazit-index.html', {'reports':reports})
    else:
        reports = Report.objects.all().order_by('date')
        return render(request, 'zobrazit-index.html', {'reports': reports})
