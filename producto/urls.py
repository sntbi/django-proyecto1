# from django.urls import path
# from . import views

# urlpatterns = [
#     path('zapatillas1/', views.Zapatillas.as_view, name='zapatillas')
# ]


from django.urls import path
from .views import ZapatillasView

urlpatterns = [
    path('producto/zapatilla', ZapatillasView.as_view(), name='zapatillas'),
]