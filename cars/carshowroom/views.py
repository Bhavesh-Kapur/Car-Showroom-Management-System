from django.shortcuts import render,redirect
from carshowroom.models import Car,Customer,Query
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import os

# Create your views here.
def admindashboard(request):
    return render(request,'admindashboard.html')

def addcar(request):
    if request.method=='POST':
        c = Car()
        c.make = request.POST.get('make')
        c.model = request.POST.get('model')
        c.year = request.POST.get('year')
        c.price = request.POST.get('price')

        if len(request.FILES)!= 0:
            c.img = request.FILES['image']
        c.save()
        messages.success(request, f'New Car added to inventory' ,extra_tags='posted')
        return redirect('addcar')
    return render(request, 'addcar.html')

    #     make=request.POST.get('make')
    #     model=request.POST.get('model')
    #     year=request.POST.get('year')
    #     price=request.POST.get('price')
    #     img=request.POST.get('image')
    #     car=Car(make=make,model=model,year=year,price=price,img=img)
    #     car.save()
    #     
    # return render(request,'addcar.html')


def viewinventory(request):
    cars=list(Car.objects.all())   #Cars.objects.filter(make='hyundai')
    dic={'cars':cars}
    return render(request,'viewinventory.html',dic)



def addcustomer(request):
    if request.method=='POST':
        c = Customer()
        c.name=request.POST.get('name')
        c.email=request.POST.get('email')
        c.phone=request.POST.get('phone')
        c.address=request.POST.get('address')
        c.save()
        print(c.name,c.email,c.phone,c.address)
    
    return render(request,'addcustomer.html')


def manageorders(request):
    return render(request,'manageorders.html')



def about(request):
    return render(request,'about.html')

def catalogue(request):
    return render(request,'catalogue.html')


def featured(request):
    return render(request,'featured.html')



def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        doubt=request.POST.get('message')
        query=Query(name=name,phone=phone,email=email,doubt=doubt)
        query.save()
        messages.success(request, f'Query Submitted Sucessfully' ,extra_tags='posted')
        print(name,email,phone,doubt)
    return render(request,'contact.html')


def login(request):
    return render(request, 'login.html')



def adminlogin(request):
    return render(request, 'adminlogin.html')

# def adminlogin(request):
#     if not request.user.is_anonymous:
#         return redirect("admindashboard")
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('admindashboard')
#         return render(request, 'adminlogin.html', {'error_message': 'Invalid credentials'})

#     return render(request, 'adminlogin.html')



def viewcontacts(request):
    doubt=list(Query.objects.all())   #Cars.objects.filter(make='hyundai')
    dic={'doubt':doubt}
    print(dict)
    return render(request,'viewcontacts.html',dic)
    
    # return render(request, 'viewcontacts.html')


def editpage(request, pk):
    c = Car.objects.get(model=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(c.img)>0:
                os.remove(c.img.path)
            c.img = request.FILES['image']
        c.make = request.POST.get('make')
        c.model = request.POST.get('model')
        c.year = request.POST.get('year')
        c.price = request.POST.get('price')

        c.save()
        messages.success(request, "Car details updated")
        return redirect('viewinventory')
    dic={"c":c}
    return render(request, 'editpage.html', dic)



def edit(request):
    redirect('viewinventory')
