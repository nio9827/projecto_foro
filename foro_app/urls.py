from . import views
from django.urls import path

urlpatterns = [
    path ('plantilla',views.Plantilla, name='plantilla'),
    path ('',views.home, name='home'),
]
