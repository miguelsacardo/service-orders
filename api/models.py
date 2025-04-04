from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# User is a model provided by Django
# here, I only add the Role field in default fields that User model has
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin',   'Admin'),
        ('manutentor', 'Manutentor'),
        ('user', 'User')
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

