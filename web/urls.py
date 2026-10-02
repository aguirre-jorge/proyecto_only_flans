from django import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    #secciones
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    #usuarios
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='flanes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]