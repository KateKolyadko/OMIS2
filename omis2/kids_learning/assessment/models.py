from django.db import models
from user_profile.models import ChildProfile  
from content.models import Lesson

class Assessment(models.Model):
    child_profile = models.ForeignKey(ChildProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.IntegerField()
    comments = models.TextField()
