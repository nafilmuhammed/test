from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=300)
    price=models.FloatField(max_length=255)
    stock=models.ImageField()
    image=models.CharField(max_length=3000)



class offer(models.Model):
    code=models.IntegerField()
    offer=models.CharField(max_length=300)
    image=models.CharField(max_length=4000)

