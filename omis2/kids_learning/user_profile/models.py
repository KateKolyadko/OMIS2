from django.db import models
from django.contrib.auth.models import User
import json

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ChildProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Interest, blank=True) 
    level = models.CharField(max_length=50)
    progress_history = models.TextField(default='{}')

    def __str__(self):
        return self.user.username

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    child_profile = models.ForeignKey(ChildProfile, related_name='achievements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title