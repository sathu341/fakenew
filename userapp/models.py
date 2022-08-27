from django.db import models

# Create your models here.
class User_tbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Predict_tbl(models.Model):
     userid=models.IntegerField(max_length="10")
     headline=models.TextField(max_length=100)
     result=models.CharField(max_length=100)
     dt=models.DateField(auto_now=True)

     def __str__(self):
        return self.headline