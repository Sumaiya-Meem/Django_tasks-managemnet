from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def sign_up(request):
   
   form = CustomRegisterForm()
   if request.method=="POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "🎉 Account created successfully!")
        else:
            print("Form is not valid")
   context = {'form': form}
   return render(request,'registration/register.html',context)

def sign_in(request):
   if request.method=='POST':
      # print(request.POST)
      username=request.POST.get('username')
      password=request.POST.get('password')
      
      user=authenticate(request,username=username,password=password)
      print(user)
      
      if user is not None:
         login(request,user)
         return redirect('home')
      
   return render(request,'registration/login.html')


def log_out(request):
   if request.method=='POST':
      logout(request)
      return redirect('sign-in')
   


