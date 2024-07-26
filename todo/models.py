'''importing model from database and user'''
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    '''A model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
