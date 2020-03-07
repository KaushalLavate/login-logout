from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'base.html',{'name':'Kaushal'});

def add(request):
    sum1=0
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    sum1=val1+val2
    print(sum1)
    return render(request,'base.html',{'result':sum1});