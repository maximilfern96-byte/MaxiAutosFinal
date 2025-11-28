
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUsuarioView.as_view(), name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/', views.perfil_usuario, name='perfil'),
]
