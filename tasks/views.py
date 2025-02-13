from django.shortcuts import render
from django.http import HttpResponse
from tasks.form import TaskModelForm
from tasks.models import Employee
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
                  return render(request, "task_form.html",{"form": task_form,"message":"task added successfully"})
                  
                  
    context = {"form": task_form}
    return render(request, "task_form.html", context)


