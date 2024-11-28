from django.urls import path

from . import views

urlpatterns = [
    path('report', views.report, name='report-posty'),
    path('zobrazit', views.zobrazit, name='zobrazit-posty'),
]