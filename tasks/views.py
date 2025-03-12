from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.form import TaskModelForm,TaskDetailModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):
# getting all task count
   # pending_task=Task.objects.filter(status="PENDING").count()
   
   type=request.GET.get('type','all')
   # print(type)
# optimize getting all task count
   counts=Task.objects.aggregate(
            total=Count('id'),
            completed_task=Count('id',filter=Q(status='COMPLETED')),
            process_task=Count('id',filter=Q(status='IN_PROGRESS')),
            pending_task=Count('id',filter=Q(status='PENDING')),
            )
   
   # retriving task data
   based_query=tasks=Task.objects.select_related('details').prefetch_related('assigned_to')
   
   if type=='completed_task':
      tasks=based_query.filter(status="COMPLETED")
   elif type=='process_task':
      tasks=based_query.filter(status="IN_PROGRESS")
   elif type=='pending_task':
      tasks=based_query.filter(status="PENDING")
   elif type=='all':
      tasks=based_query.all()
   
   
   context={
            "tasks":tasks,
            "total_tasks":counts
   } 
   return render(request,"dashboard/manager_dashboard.html",context)



def user_dashboard(request):
   return render(request,"dashboard/user_dashboard.html")

def create_task(request):
#     employees = Employee.objects.all()  # Fetch all employees
    task_form = TaskModelForm()
    task_detail_form=TaskDetailModelForm()
    
    if request.method =='POST':
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        
        if task_form.is_valid() and task_detail_form.is_valid():
                  task=task_form.save()
                  task_detail=task_detail_form.save(commit=False)
                  task_detail.task=task
                  task_detail.save()
                  
                  messages.success(request,"Task created successfully")
                  return redirect('create-task')
                  
                  
    context = {"task_form": task_form,"task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)

def update_task(request,id):
    task=Task.objects.get(id=id)
    
    task_form = TaskModelForm(instance=task)
    if task.details:
       task_detail_form=TaskDetailModelForm(instance=task.details)
    
    if request.method =='POST':
        task_form = TaskModelForm(request.POST,instance=task)
        task_detail_form = TaskDetailModelForm(request.POST,instance=task.details)
        
        if task_form.is_valid() and task_detail_form.is_valid():
                  task=task_form.save()
                  task_detail=task_detail_form.save(commit=False)
                  task_detail.task=task
                  task_detail.save()
                  
                  messages.success(request,"Task updated successfully")
                  return redirect('update-task',id)
                  
                  
    context = {"task_form": task_form,"task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)

def delete_task(request,id):
   if request.method=='POST':
      task=Task.objects.get(id=id)
      task.delete()
      
      messages.success(request,'Task deleted successfully')
      return redirect('manager-dashboard')
   else:
    messages.error(request,"Something went wrong")
    return redirect('manager-dashboard')
      
def view_task(request):
   tasks = Task.objects.filter(project_id=1).prefetch_related('assigned_to')
   return render(request, "show_task.html", {"tasks": tasks})

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


#      task_count=Task.objects.aggregate(num_task=Count('id'))

#      projects=Project.objects.annotate(num_task=Count('task')).order_by('num_task')
#      return render(request,"show_task.html",{"projects":projects})
     
     


