from django.db import models

class login(models.Model):
    username = models.CharField(max_length=200)
    passwords = models.CharField(max_length=200)

    def __str__(self):
        return self.username

