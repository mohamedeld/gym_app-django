from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Exercises
from .serializers import StorySerializers
# Create your views here.
class UserExercises(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializers