
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('producto/', include('producto.urls')),
    path('usuarios/', include('usuarios.urls')),
]
