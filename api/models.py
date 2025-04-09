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

class Manager(models.Model):    
    ni = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_account")

class Maintainer(models.Model):
    ni = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="maintainer_account")
    manager = models.ForeignKey(Manager, verbose_name="Manager of Maintainers", on_delete=models.CASCADE, default=1)


class Responsible(models.Model):
    ni = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

class Environment(models.Model):
    ni = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

class Patrimony(models.Model):
    ni = models.CharField(max_length=15)
    description = models.TextField()
    location = models.CharField(max_length=100)