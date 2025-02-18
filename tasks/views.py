from django.shortcuts import render
from django.http import HttpResponse
from tasks.form import TaskModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

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
#      tasks=Task.objects.all()
     
#      #retrieve specific task
#      task3=Task.objects.get(id=3)


# show the tasks which is pending
#      tasks=Task.objects.filter(status="PENDING")
     
# show the tasks which is pdue date is today
#      tasks=Task.objects.filter(due_date=date.today())


# show the task details which priority is not low
#     tasks=TaskDetail.objects.exclude(priority="L")
     
 
# show the task details which status is pending or progess
#      tasks=Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
     
#      select related field (ForeignKey,OnetoOneField)
#      OnetoOneField
#      tasks=TaskDetail.objects.select_related('task').all()
     
     #      ForeignKey ()
#      tasks=Task.objects.select_related('project').all()

#       prefetch_related work on (reverse ForeignKey)
#      tasks=Project.objects.prefetch_related('task_set').all()


#       prefetch_related work on  ManytoMany
#      tasks=Task.objects.prefetch_related('assigned_to').all()

#      task_count=Task.objects.aggregate(num_task=Count('id'))

     projects=Project.objects.annotate(num_task=Count('task')).order_by('num_task')
     return render(request,"show_task.html",{"projects":projects})
     
     


