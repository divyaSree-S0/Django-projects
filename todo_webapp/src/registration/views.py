from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .models import TaskListItems,TaskAssigned,User      #,CustomUser


global user_profile
# Create your views here.
def loginView(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(username=username,password=pass1)
        messages.set_level(request,messages.ERROR)
        # print(user)
        # print(type(user))
        if user is not None:
            login(request,user)
            # return render(request,'userpage.html')
            return redirect('user_page')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'login.html')

# def userloginView(request):
#     return render(request,'userpage.html')
def userloginView(request):
    # Get the logged-in user
    current_user = request.user
    # Retrieve tasks assigned to the current user
    user_tasks = TaskAssigned.objects.filter(user_profile=current_user)
    # no_tasks_message = 'No tasks assigned yet' if user_tasks.count() == 0 else None
    #print(user_tasks,"\n",user_tasks[0],current_user, user_tasks.count())
    # if user_tasks.count() == 0:
    #     current_user.user_tasks.all().task.content = 'No tasks assigned'
    if user_tasks.exists():
        # User has tasks
        return render(request, 'userpage.html', {'user': current_user, 'tasks': user_tasks})
    else:
        # User has no tasks
        no_tasks_message = 'No tasks assigned'  # Define the message
        return render(request, 'userpage.html', {'user': current_user, 'no_tasks_message': no_tasks_message})
    #return render(request, 'userpage.html', {'user': current_user, 'tasks': user_tasks, 'no_tasks_message': no_tasks_message})

def signupView(request):
    if request.method=='POST':
        uname = request.POST['username']
        # x=request.POST.get('username')
        # users = User(username=x)
        # users.save()
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        messages.set_level(request,messages.ERROR)
        if pass1!='' and pass1!=pass2:
            messages.error(request,'Password does not match')   
            return render(request,'signup.html')      
        else:
            new_user = User.objects.create_user(username=uname,email=email,password=pass1)
            login(request,new_user)
            # new_user.save()
            # user_profile=User.objects.create(username=new_user)
            # user_profile.save()
            return redirect('login')

            # return render(request,'signup.html')
        # print(f'User Created:{uname}\t{email}\t{pass1}\t{pass2} ',new_user)
    return render(request,'signup.html')


def adminloginView(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        #user=authenticate(username=username,password=pass1)
        if username=='admin' and pass1=='admin':
        #if user is not None:
            # login(request,username)
            # print(User.objects.all())
            # print(type(User.objects.all()))
            # for user in User.objects.all():
            #     print(user.username,user.id)
            return redirect('add_task')
        else:
            messages.add_message(request,20,'Invalid Credentials')
    return render(request,'adminlogin.html')

def taskView(request):
    all_tasks=TaskListItems.objects.all()
    return render(request,'homepage.html',{'all_items':all_tasks})

def addTaskView(request):
    if request.method=='POST':
        user_id= request.POST.get('user')
        print(user_id) #request.POST.get('user')
        task_content=request.POST.get('add_task')
        # for current_user in User.objects.all():
        #     user_tasks = TaskAssigned.objects.filter(user_profile=current_user)
        #     if user_tasks.exists():
        #          return render(request, 'adminpage.html',{'users':User.objects.all()})
        #     else: 
        #         no_tasks_message = 'No tasks assigned'  # Define the message
        #         return render(request, 'adminpage.html', {'user': current_user, 'no_tasks_message': no_tasks_message})  
        try:
            user = User.objects.get(id=user_id)
            new_task = TaskListItems.objects.create(content=task_content)
            task_assigned = TaskAssigned.objects.create(user_profile=user,task=new_task)
            task_assigned.save()
            # print(f'Hello{task_assigned}{task_content}{user}{user_id}{User}')
            #user.tasklistitems_set.add(new_task)
        # x = request.POST['content']
        # new_task = TaskListItems(content=x)
        # new_task.save()
            return HttpResponseRedirect('/add_task/')            #change this 
        except:
            messages.error(request,'User does not exist')
    return render(request,'adminpage.html',{'users':User.objects.exclude(username='admin')})

def deleteTaskView(request,i):
    task_to_delete=TaskListItems.objects.get(id=i)
    task_to_delete.delete()
    return HttpResponseRedirect('/add_task/')


def logoutView(request):
    logout(request)
    return redirect('login')

def usersListView(request):
    all_users=User.objects.all()
    return render(request,'users.html',{'all_users':all_users})

# def homeView(request):
#     return render(request,'home.html')
