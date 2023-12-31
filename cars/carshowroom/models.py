from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to="images/", null=True, default=None)
    des = models.CharField(max_length=1000, default='Default Description')

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

class Query(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    doubt=models.CharField(max_length=400)

class TestDrive(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date = models.DateField()
    status = models.BooleanField(default=False)

class BookingCar(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    date = models.DateField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)