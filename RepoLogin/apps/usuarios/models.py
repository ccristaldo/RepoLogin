from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    provincia = models.CharField(max_length=30, null=True)
    ciudad = models.CharField(max_length=30, null=True)
    universidad = models.CharField(max_length=50, null=True)
    carrera = models.CharField(max_length=50, null=True)
    pass