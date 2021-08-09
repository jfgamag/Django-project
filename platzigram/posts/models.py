from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    fist_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
