from django.db import models


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Leaders(models.Model):
    username=models.CharField(max_length=250)
    photo=models. ImageField(upload_to='pics')
    intro=models.TextField()