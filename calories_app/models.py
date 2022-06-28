from django.db import models
from meals_app.models import Meal
# Create your models here.
class Calories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Image = models.ImageField(upload_to="calories/",blank=True)
    quantity_grams = models.IntegerField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    