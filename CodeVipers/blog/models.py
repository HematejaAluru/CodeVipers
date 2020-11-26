from django.db import models

# Create your models here.
class Post(models.Model):
    name= models.CharField(max_length=100)
    question=models.TextField()
    postimage=models.ImageField(blank=True)
   
    
class reply(models.Model):
    name=models.CharField(max_length=100)
    connector=models.IntegerField()
    reply=models.TextField()
    replyimage=models.ImageField(blank=True)

