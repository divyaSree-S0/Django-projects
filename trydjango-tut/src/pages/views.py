from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user,args,kwargs)
    return render(request,"home.html",{})   