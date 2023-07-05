from django.db import models

# Create your models here.


class User(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname, self.email
