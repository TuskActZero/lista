from django.db import models

# Create your models here.

class Lista(models.Model):
    nombre = models.CharField(max_length=30, default="Pepo")
    opinion = models.TextField(default="aca ba una opinion de prueba")
    email = models.EmailField(default="example@gmail.com")


