from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ),
    path('posts/', include('posty.urls'))
]
