from django.shortcuts import render
from .models import ToDoListItems
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    all_tasks=ToDoListItems.objects.all()
    return render(request,'homepage.html',{'all_items':all_tasks})

def addTodoView(request):
    x = request.POST['content']
    new_task = ToDoListItems(content=x)
    new_task.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request,i):
    y = ToDoListItems.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

# def loginView(request):
#     return render(request,'login.html')
