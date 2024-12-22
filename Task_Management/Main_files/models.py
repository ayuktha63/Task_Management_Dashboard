

# Create your models here.
from django.db import models

class Task(models.Model):
    # Task Name
    name = models.CharField(max_length=200)
    
    # Task Description (Optional)
    description = models.TextField(blank=True, null=True)
    
    # Status of the task (Pending or Completed)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    # Due Date (Optional)
    due_date = models.DateTimeField(null=True, blank=True)
    
    # Priority of the task (Optional)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the task (for admin view or shell)
    def __str__(self):
        return self.name
