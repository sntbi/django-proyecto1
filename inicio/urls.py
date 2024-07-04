from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path('template1/<str:nombre>/<str:apellido>/<edad>/', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<edad>/', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<edad>/', views.template3),
    path('template4/<str:nombre>/<str:apellido>/<edad>/', views.template4),
    path('probando/', views.probando),
    path('alumnos/crear/<str:nombre>/<str:apellido>/', views.crear_alumno),
]
