from django.db import models
from users.models import User

# Create your models here.


class File(models.Model):
    file_name = models.CharField(max_length=500)
    file_size = models.CharField(max_length=20)
    file_link = models.CharField(max_length=200)
    user_id = models.ForeignKey(
        User, related_name='user_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.file_link, self.user_id
