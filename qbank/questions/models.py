from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
        question = models.CharField(max_length=100)
        answer = models.CharField(max_length=250, blank=True)
        created = models.DateTimeField(auto_now_add=True)
        datecompleted = models.DateTimeField(null=True, blank=True)
        important = models.BooleanField(default=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.question
