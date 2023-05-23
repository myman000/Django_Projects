from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    task_Name = models.CharField(max_length=1000)
    dateTime = models.DateTimeField()
    priority = models.CharField(max_length=200)
