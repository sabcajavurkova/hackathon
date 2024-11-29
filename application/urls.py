from django.urls import path
from .views import BluetoothDataView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prihlaseni/', views.login, name='login'),
    path('tvorba-uctu/', views.signup, name='signup'),
    path('bluetooth/', BluetoothDataView.as_view(), name='bluetooth-data'),

]