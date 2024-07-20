from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField() "this field is auto ceated by dango"
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    adress = models.TextField(null = True, blank = True)



class Car(models.Model):
    car_name = models.CharField(max_length = 100)
    speed = models.IntegerField(default = 50)