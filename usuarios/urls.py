from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html') , name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/<int:id>/ver/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_pass'),
    path('aboutme/', views.aboutme, name='aboutme'),
]
