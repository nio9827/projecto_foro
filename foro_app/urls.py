from . import views
from django.urls import path

urlpatterns = [
    path ('plantilla',views.Plantilla, name='plantilla'),
    path ('',views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),


]
