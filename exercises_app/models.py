from django.db import models

# Create your models here.
class Exercises(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="exercises_app/")
    