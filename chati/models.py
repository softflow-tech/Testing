from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class User(models.Model):

class Group(models.Model):
    group_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    group_members = models.ManyToManyField()