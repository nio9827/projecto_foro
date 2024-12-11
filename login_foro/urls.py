from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, dashboard_view

urlpatterns = [
    # Inicio de sesión
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Cierre de sesión
    path('login/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # Registro de usuarios
    path('register/', register_view, name='register'),
    # Panel de control
    path('foro_app/Home.html', dashboard_view, name='Home'),
]