from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FutureVision(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    vision_text = models.TextField()

    def __str__(self):
        return self.name