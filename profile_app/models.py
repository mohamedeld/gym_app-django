from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile_name")
    gender = models.CharField(max_length=10,blank=True)
    image = models.ImageField(upload_to="profiles/",blank=True)
    is_active =models.BooleanField(default=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    amount_of_water = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username
