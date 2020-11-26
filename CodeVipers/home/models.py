from django.db import models
class register(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=100)
class posts12(models.Model):
    username=models.CharField(max_length=200)
    userform=models.TextField()



     