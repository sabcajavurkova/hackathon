from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prihlaseni/', views.login, name='login'),
    path('tvorba-uctu/', views.signup, name='signup'),
]