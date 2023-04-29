from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=70)
    description = models.TextField(max_length=255)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.task
    