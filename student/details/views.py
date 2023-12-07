from django.shortcuts import render
from details.models import details 

# Create your views here.
def select(request):
    stud = details.objects.all();
    return render(request,'select.html',{'data':stud})