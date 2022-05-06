from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Story(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    story_image = models.ImageField(upload_to="story/",null=True)
    title = models.CharField(max_length=255,blank=True)
    description = models.TextField(max_length=1000,blank=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title