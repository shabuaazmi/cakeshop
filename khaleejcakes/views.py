from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
    # return render(request,'sellerpage.html')

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def seller(request):
    return render(request,'sellerpage.html')
def userform1(request):
    a=User()
    a.first_name=request.Post.get('fname')
    a.username=request.Post.get('username')
    a.email=request.Post.get('email')
    p=request.Post.get('password')
    a.set_password(p)
    a.save()
    return redirect('/')
def login1(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=authenticate(username=username,password=password)
    if data is not None and data.is_superuser==1:
        return redirect('/adminpage/')
    elif data is not None and data.is_superuser==0:
        return redirect('/userpage/')
    else:
        return HttpResponse('invalid-response')
def adminpage(request):
    return render(request,'admin.html')
def userpage(request):
    return render(request,'userpage.html')
    
# Create your views here.
