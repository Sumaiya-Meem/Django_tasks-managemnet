from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user = request.user  
    # print("Logged-in User:", user)  
    return render(request, 'home.html', {'user': user})

def no_permission(request):
    return render(request,'no_permission.html')