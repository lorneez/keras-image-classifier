from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(max_length=200, default="name is null")
    email = models.CharField(max_length=200, default="email is null")
    password = models.CharField(max_length=200, default="password is null")
    def __str__(self):
        return self.name

class Image(models.Model):
    file = models.FileField(upload_to='uploads/')
