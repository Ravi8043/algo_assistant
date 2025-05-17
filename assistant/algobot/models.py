from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question
