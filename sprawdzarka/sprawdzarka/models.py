from django.db import models



class Student(models.Model):
    snumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()

#ta baze danych
class SendedTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/SendedTasks/')

