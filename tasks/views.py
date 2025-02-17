from django.shortcuts import render
from django.http import HttpResponse
from tasks.form import TaskModelForm
from tasks.models import Task
# Create your views here.

def manager_dashboard(request):
   return render(request,"dashboard/manager_dashboard.html")

def user_dashboard(request):
   return render(request,"dashboard/user_dashboard.html")

def create_task(request):
#     employees = Employee.objects.all()  # Fetch all employees
    task_form = TaskModelForm()  
    
    if request.method =='POST':
        task_form = TaskModelForm(request.POST)
        
        if task_form.is_valid():
                  task_form.save()
                  task_form = TaskModelForm()
                  return render(request, "task_form.html",{"form": task_form,"message":"task added successfully"})
                  
                  
    context = {"form": task_form}
    return render(request, "task_form.html", context)

def view_task(request):
                  # retrive all data from tasks model
     tasks=Task.objects.all()
     
     #retrieve specific task
     task3=Task.objects.get(id=3)
     return render(request,"show_task.html",{"tasks":tasks,"task3":task3})
     


