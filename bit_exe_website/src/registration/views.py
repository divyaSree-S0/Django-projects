from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def LoginView(request):
    return render(request,'login.html')

def SignupView(request):
    return render(request,'signup.html')

def HomepageView(request):
    return render(request,'homepage.html')

def LoginSliderView(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print(username,password)
        return render(request,'index.html')
    else:
        messages.error(request,"Invalid Credentials")

    return render(request,'login-slider.html')

def RegisterView(request):
    return render(request,'register.html')

def IndexView(request):
    return render(request,'index.html')