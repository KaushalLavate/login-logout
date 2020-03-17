from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            err='loged In SuccessFully'
            return redirect('/')
        else:
            err='Invalid credencials'
            return render(request,'login.html',{'err':err})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        comfirm_password=request.POST['C_password']
        email=request.POST['email']
        if password==comfirm_password:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                err='Username taken'
                return render(request,'register.html',{'err':err})
            elif User.objects.filter(email=email).exists():
                print('Email taken')
                err='Email taken'
                return render(request,'register.html',{'err':err})
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('User Created')
                return render(request,'login.html')
        else:
            err='Password incorrect'
            print('Incorrect password')
            return render(request,'register.html',{'err':err})
    else:
        return render(request,'register.html')
