from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manager_dashboard(request):
   return render(request,"dashboard/manager_dashboard.html")

def user_dashboard(request):
   return render(request,"dashboard/user_dashboard.html")

def create_task(request):
    return render(request,"task_form.html")


