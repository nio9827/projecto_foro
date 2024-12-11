from django.contrib.auth.models import AbstractUser
from django.db import models

# Definición de roles de usuario
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('administrador', 'Administrador'),
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='estudiante')
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
    
    def get_full_role(self):
        return self.get_role_display()