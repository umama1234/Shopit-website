import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Customer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,default='',null=True,blank=True)
    address=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.firstname,self.lastname
    


class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(default=0,max_digits=6,decimal_places=2)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.name



class Order(models.Model):
    product=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    phonenumber=models.CharField(max_length=20)
    quantity=models.IntegerField(default=1)
    date=models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.product