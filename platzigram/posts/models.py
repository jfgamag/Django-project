from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    country = models.CharField(max_length=30, default='Colombia')


    bio = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)

    birthdate = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
