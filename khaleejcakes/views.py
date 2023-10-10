from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from khaleejcakes.models import table_user
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
def signup1(request):
    a=User()
    f=table_user()
    f.first_name=request.POST.get('fname')
    f.email=request.POST.get('email')
    
    a.first_name=request.POST.get('fname')
    a.username=request.POST.get('username')
    a.email=request.POST.get('email')
    p=request.POST.get('password')
    a.set_password(p)
    a.save()
    return redirect('/login/')
def login1(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    # request.session['username']=b
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
    # s=request.session['username']
    # return render(request,'userpage.html',{'x':s})
    return render(request,'userpage.html')
def userprofile(request):
    return render(request,'userprofile.html')
    
# Create your views here.
