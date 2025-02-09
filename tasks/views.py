from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to task management project")

def show_task(request):
    return HttpResponse("This is our show task page")

def show_specific_task(request,id):
    print("id",id)
    return HttpResponse(f"This is my specific {id} task")
