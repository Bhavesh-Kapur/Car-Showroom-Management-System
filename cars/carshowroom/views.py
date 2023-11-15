from django.shortcuts import render
from carshowroom.models import Car,Customer

# Create your views here.
def admindashboard(request):
    return render(request,'admindashboard.html')

def addcar(request):
    if request.method=='POST':
        make=request.POST.get('make')
        model=request.POST.get('model')
        year=request.POST.get('year')
        price=request.POST.get('price')
        car=Car(make=make,model=model,year=year,price=price)
        car.save()
    return render(request,'addcar.html')


def viewinventory(request):
    return render(request,'viewinventory.html')


def addcustomer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        customer=Customer(name=name,phone=phone,email=email,address=address)
        customer.save()
        # print(name,email,phone,address)
    
    return render(request,'addcustomer.html')


def manageorders(request):
    return render(request,'manageorders.html')