# from django.urls import path
# from . import views

# urlpatterns = [
#     path('zapatillas1/', views.Zapatillas.as_view, name='zapatillas')
# ]


from django.urls import path
from .views import ZapatillasView, CrearZapatilla, VerZapatilla

urlpatterns = [
    path('zapatilla/', ZapatillasView.as_view(), name='zapatillas'),
    path('zapatilla/crear', CrearZapatilla.as_view(), name='crear_zapatilla'),
    path('zapatilla/<int:pk>', VerZapatilla.as_view(), name='ver_zapatilla'),
]