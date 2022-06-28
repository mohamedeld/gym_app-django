from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Calories
from .serializers import StorySerializers
# Create your views here.
class UserCalories(viewsets.ModelViewSet):
    queryset = Calories.objects.all()
    serializer_class = CaloriesSerializers