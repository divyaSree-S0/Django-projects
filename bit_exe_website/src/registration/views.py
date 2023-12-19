# from django import forms
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import check_password,make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.db.models import Max
from django.contrib import messages
from .forms import LoginForm,SignupForm
from .models import Users, Conveyors

# counter = 1


# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        # form = SignupForm(request.POST)
        # if form.is_valid():
            # username = request.POST.get('user')
        # email = form.cleaned_data.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        try:
                user = Users.objects.get(username=username)
        except Users.DoesNotExist:
                user = None
        if user and check_password(password, user.password):
        # if user and user.passw == password:
                request.session['username'] = username
                login(request,user)
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('pass1')
        email = request.POST.get('email')
        industry_name = request.POST.get('industry_name')
        mine_location = request.POST.get('mine_location')
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            max_id = Users.objects.all().aggregate(Max('_id'))['_id__max']
            if max_id is None:
                max_id = 0 
            user_data = Users.objects.create(
                    _id = max_id + 1,
                    username=username,
                    password=password,
                    email=email,
                    industry_name=industry_name,
                    mine_location=mine_location,
                    collection_name=username+"1"
                )
            print(password)
            # user_data.save()    # running this line after User.objects.create() gives error because it hashes the already hashed password again , updates previousone
            return redirect('login')
    return render(request,'signup.html')

def AboutView(request):
    return render(request,'about.html')

def ConveyorView(request):
    return render(request,'conveyor.html')

def ProfileView(request):
    return render(request,'profile.html')

def HomeView(request):
    return render(request,'home.html')

def RealtimeMaintenanceView(request):
    return render(request,'real_time_maintenance.html')

def CreateSystemView(request):
    if request.method=="POST":
         name = request.POST.get('name')
         totalPulleys = request.POST.get('totalPulleys')
         pulleysInShoe = request.POST.get('pulleysInShoe')
         beltLength = request.POST.get('beltLength')
         beltWidth = request.POST.get('beltWidth')
         beltThickness = request.POST.get('beltThickness')
         mine = request.POST.get('mine')
         industry = request.POST.get('industry')
        #  print(name,totalPulleys,pulleysInShoe,beltLength,beltWidth,beltThickness,mine,industry)
        #  smttg = Users.objects.get(username=request.session['username'])
        #  print(smttg._id) 
         user = Users.objects.get(username=request.session['username'])
         print(user)
         try:
            conveyor = Conveyors.objects.create(
                    userId=user,
                    name=name,
                    totalPulleys=totalPulleys,
                    pulleysInShoe=pulleysInShoe,
                    beltLength=beltLength,
                    beltWidth=beltWidth,
                    beltThickness=beltThickness,
                    mine=mine,
                    industry=industry,
            )
            conveyor.save()
            # if user.noConveyorSystem is None:
            #     user.noConveyorSystem = 0
            print(user.noConveyorSystem,user.noConveyorSystem+1)
            user.noConveyorSystem += 1
            user.save()
            # number_system = Users.objects.update(noConveyorSystem=user.noConveyorSystem+1)
            # number_system.save()
            print("success")
         except TypeError as e:
           print(f"System added: {e}")
           messages.error(request, "There was an error saving the conveyor. Please try again.")
           if user.noConveyorSystem is None:
                user.noConveyorSystem = 0
           user.noConveyorSystem += 1
           user.save()
        #         user.noConveyorSystem = 0
        #    print(user.noConveyorSystem,user.noConveyorSystem+1)
        #    number_system = Users.objects.update(noConveyorSystem=user.noConveyorSystem+1)
        #    number_system.save()
         
    return render(request,'create.html')

def SystemDetailsView(request):
    return render(request,'system_details.html')

def UserPageView(request):
    return render(request,'userpage.html')

def LogoutView(request):
    logout(request)
    return redirect('')