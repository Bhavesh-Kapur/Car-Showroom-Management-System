from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    rate=models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
