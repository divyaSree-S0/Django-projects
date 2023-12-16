# from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render,redirect
from django.db.models import Max
from django.contrib import messages
from .forms import LoginForm,SignupForm
from .models import Users

# counter = 1


# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        # form = SignupForm(request.POST)
        # if form.is_valid():
            # username = request.POST.get('user')
        # email = form.cleaned_data.get('email')
        username = request.POST.get('user')
        password = request.POST.get('passw')
        print(username,password)
        try:
                user = Users.objects.get(user=username)
        except Users.DoesNotExist:
                user = None
        print(user,user.passw)
        if user and check_password(password, user.passw):
                print("yes")
        # if user and user.passw == password:
                request.session['username'] = username
                return redirect('userpage')
        # user = AuthenticatedForm(request.POST)
        # # user = authenticate(request,username=username,password=password)
        # print(user)
        # if user is not None:
        #     login(request,user)
        #     return redirect('userpage')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def SignupView(request):
    # global counter
    # print(counter)
    if request.method == 'POST':
        # form = SignupForm(request.POST)
        # if form.is_valid():
            # username = request.POST.get('user')
        # email = form.cleaned_data.get('email')
        username = request.POST.get('user')
        password = request.POST.get('passw')
        confirm_password = request.POST.get('pass1')
        email = request.POST.get('email')
        industry_name = request.POST.get('industry_name')
        mine_location = request.POST.get('mine_location')
        print(username,password,confirm_password,email,mine_location)
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            max_id = Users.objects.all().aggregate(Max('_id'))['_id__max']
            if max_id is None:
                max_id = 0 
            user_data = Users.objects.create(
                    _id = max_id + 1,
                    user=username,
                    passw=password,
                    email=email,
                    industry_name=industry_name,
                    mine_location=mine_location,
                    collection_name=username+"0"
                )
            user_data.save()
                # print(user_data)
            return redirect('login')
    return render(request,'signup.html')

def AboutView(request):
    return render(request,'about.html')

def ConveyorView(request):
    return render(request,'conveyor.html')

def ProfileView(request):
    return render(request,'profile.html')

def HomeView(request):
    if request.method == 'POST':
        print("?")
        # form = LoginForm(request.POST)
        print("?0")
        # if form.is_valid():
        print("?8")
        username = request.POST.get('user')
        password = request.POST.get('passw')
        # username = form.cleaned_data['user']
        # password = form.cleaned_data['pass']
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'home.html')

def RealtimeMaintenanceView(request):
    return render(request,'real_time_maintenance.html')

def SystemDetailsView(request):
    return render(request,'system_details.html')

def UserPageView(request):
    return render(request,'userpage.html')