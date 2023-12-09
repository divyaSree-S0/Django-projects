from django import forms
from django.contrib.auth import login,authenticate
from django.shortcuts import render
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('user')
            password = request.POST.get('pass')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfull")
            else:
                messages.error(request,"Invalid Credentials")
            print(username,password)
    else:
        form = LoginForm()

    return render(request,'login.html')

def IndexView(request):
    return render(request,'index.html')
def indexview(request):
    return render(request,'index-an.html')

def ABoutView(request):
    return render(request,'about.html')

def ContactView(request):
    return render(request,'contact.html')