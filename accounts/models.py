from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
