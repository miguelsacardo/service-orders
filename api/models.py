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
    ni = models.CharField(max_length=15, default="sn1")
    name = models.CharField(max_length=255, default="User")
    area = models.CharField(max_length=255, default="Area")
    cargo = models.CharField(max_length=255, default="Cargo")
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_account")

class Maintainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="maintainer_account")

    # gestor
    manager = models.ForeignKey(Manager, verbose_name="Manager of Maintainers", on_delete=models.CASCADE, default=1)

class Responsible(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="normal_account", default=1)

class Environment(models.Model):
    ni = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

class Patrimony(models.Model):
    ni = models.CharField(max_length=15, blank=True, null = True)
    description = models.TextField()
    location = models.CharField(max_length=100)

class ServiceOrder(models.Model):
    STATUS = (
        ('iniciada', 'Iniciada'),
        ('andamento', 'andamento'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    )

    PRIORITY = (
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baixa', 'Baixa')
    )
    description = models.TextField()
    opening = models.DateTimeField()
    closing = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS)

    patrimony = models.ForeignKey(Patrimony, on_delete=models.CASCADE, blank=True, null=True, default=None)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    maintainer = models.ForeignKey(Maintainer, on_delete=models.CASCADE)
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE, blank=True, null=True, default=None)
    priority = models.CharField(max_length=15, choices=PRIORITY)
