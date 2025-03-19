from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    # task_Set
    
    
    def __str__(self): 
      return self.name
    
    
class Task(models.Model):
   STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]
    
   project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)  # Many to One Relationship
#    assigned_to=models.ManyToManyField(Employee,related_name="tasks") # Many to Many Relationship
   assigned_to=models.ManyToManyField(User,related_name="tasks") 
   status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='PENDING')
   title=models.CharField(max_length=250)
   description=models.TextField()
   due_date=models.DateField()
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateField(auto_now=True)
   
   
   def __str__(self): 
      return self.title

# One to One Relationship
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task=models.OneToOneField(Task,
                              on_delete=models.DO_NOTHING,
                              related_name="details") 
    # assigned_to=models.CharField(max_length=150)
    asset = models.ImageField(upload_to='tasks_asset',  blank=True, null=True,default="tasks_asset/default_img.jpg")
    
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    notes=models.TextField(blank=True,null=True)
    
    
    def __str__(self): 
      return f"Details form TASK {self.task.title}"
  


        
        
        





