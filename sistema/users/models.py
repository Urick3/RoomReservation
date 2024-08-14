from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('manager', 'Gerente'),
        ('teacher', 'Docente'),
    )
    email = models.EmailField(unique=True)
    type_user = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_type_user_display()})"
