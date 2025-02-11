from django.db import models

# Create your models here.

class Task(models.Model):
   title=models.CharField(max_length=250)
   description=models.TextField()
   due_date=models.DateField()
   is_completed=models.BooleanField(default=False)
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateField(auto_now=True)

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
    task=models.OneToOneField(Task,on_delete=models.CASCADE)
    assigned_to=models.CharField(max_length=150)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)





