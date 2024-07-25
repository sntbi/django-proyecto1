from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('template1/<str:nombre>/<str:apellido>/<edad>/', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<edad>/', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<edad>/', views.template3),
    path('template4/<str:nombre>/<str:apellido>/<edad>/', views.template4),
    path('prueba/', views.probando, name='probando'),
    # V1
    # path('alumnos/crear/<str:nombre>/<str:apellido>/', views.crear_alumno, name='crear_alumno'),
    # V2
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alumnos/crear/', views.crear_alumno_v2, name='crear_alumno_v2'),
    path('alumnos/eliminar/<int:id>', views.eliminar_alumno, name='eliminar_alumno'),
    path('alumnos/editar/<int:id>', views.editar_alumno, name='editar_alumno'),
    path('alumnos/<int:id>/', views.ver_alumno, name='ver_alumno'),

    
]
