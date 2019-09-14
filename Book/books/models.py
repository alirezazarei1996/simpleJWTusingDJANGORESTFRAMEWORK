from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    year = models.CharField(max_length=4)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)