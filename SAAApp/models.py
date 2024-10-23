from django.db import models
from django.contrib.auth import get_user_model

# User model (students, teachers, and admins)
User = get_user_model()

class Goal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    status = models.BooleanField(True,  default=False)

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    progress_percentage = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

