from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
# Create your views here.
