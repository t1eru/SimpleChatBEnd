from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    gender = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(blank=True, null=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)