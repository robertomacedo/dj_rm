from django.contrib.auth.models import User
from django.db import models


class Membro(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_namber = models.CharField(max_length=30)
    cpf = models.CharField(max_length=20, unique=True)
    conjuge = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Doc(models.Model):
    titulo_eleitor = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



