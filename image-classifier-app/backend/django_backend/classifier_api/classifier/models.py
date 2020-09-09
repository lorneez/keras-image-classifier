from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, default="name is null")
    email = models.CharField(max_length=200, default="email is null")
    password = models.CharField(max_length=200, default="password is null")
    def __str__(self):
        return self.name


