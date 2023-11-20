from django.contrib import admin
from .models import Car,Customer,Booking,Query,TestDrive,BookingCar

admin.site.register(Car)
admin.site.register(Customer)
# admin.site.register(Booking)
admin.site.register(Query)
admin.site.register(TestDrive)
admin.site.register(BookingCar)