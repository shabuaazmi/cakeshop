from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')
    # return render(request,'admin.html')
    # return render(request,'userpage.html')
    # return render(request,'sellerpage.html')

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def seller(request):
    return render(request,'sellerpage.html')
# Create your views here.
