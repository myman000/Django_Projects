from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    dob = models.DateField()
