from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.models import User


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User,
                                  related_name='likes',blank=True)
    def __str__(self) : return self.title
