from rest_framework import serializers
from .models import Calories

class CaloriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calories
        fields = ('title','description','image','quantity_grams')