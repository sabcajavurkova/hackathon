from django.shortcuts import render

def report(request):
    return render(request, 'report-index.html')

def zobrazit(request):
    return render(request, 'zobrazit-index.html')
