from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
import re
from tasks.form import FormMixin

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
    
        for fieldname in ['username','password1','password2']:
                  self.fields[fieldname].help_text=None    
    


class CustomRegisterForm(FormMixin,forms.ModelForm):
     password=forms.CharField(widget=forms.PasswordInput)
     confirm_password=forms.CharField(widget=forms.PasswordInput)
     class Meta:
         model=User
         fields= ['username','first_name','last_name', 'email', 'password','confirm_password']
         
     
     def clean_email(self):
        email = self.cleaned_data.get("email")
        email_exists=User.objects.filter(email=email).exists()
        
        if email_exists:
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        return email
         
     def clean_password(self):
             password=self.cleaned_data.get("password")
             errors=[]
             
             if len(password)<8:
                 errors.append("password must be at least 8 character long")
             
             if not re.search(r'[A-Z]', password): 
                errors.append("Password must contain at least one uppercase letter.")

             if not re.search(r'[a-z]', password): 
               errors.append("Password must contain at least one lowercase letter.")

             if not re.search(r'[0-9]', password):  
               errors.append("Password must contain at least one number.")

             if not re.search(r'[@#$%^&+=]', password):  
                errors.append("Password must contain at least one special character (@#$%^&+=).")
             if errors:
                 raise forms.ValidationError(errors) 
             return password
        
    #  non field error
     def clean(self):
            cleaned_data=super().clean()
            
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password and confirm_password and password != confirm_password:
             raise forms.ValidationError("Passwords do not match.")

            return cleaned_data
            
             
            
         
         
         
         