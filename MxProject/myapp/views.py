from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import RegisterEmployee
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def Home(request):
    return render(request,'home.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        age = request.POST['age']
        password = request.POST['password']
        # print({"username":username,'email':email,'address':address,'age':age,'password':password})
        user = User.objects.create_user(username=email,first_name = username,email=email,password=password)
        employee = RegisterEmployee.objects.create(user=user,address=address,age=age)
        employee.save()
        return redirect('Login')
    return render(request,'signup.html')


def Login(request):
    if request.method == 'POST': 
        email = request.POST['email']       
        password = request.POST['password']
    
        user = authenticate(username=email,password=password)
        print({"email":email,'password':password})
        if user:
            login(request,user)
            return render(request,'admindash.html') 
        else :
            messages.info(request,"Invalid Credentials")
    return render(request,'login.html')

def adminpage(request):
    return render(request,'admindash.html')

def Logout(request):
    logout(request)
    return redirect('/')