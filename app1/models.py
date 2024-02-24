from django.db import models


class Employee(models.Model):
    eid = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)
    salary = models.FloatField()
    city = models.CharField(max_length=40)
    task = models.CharField(max_length=40)
