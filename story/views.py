from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Story
from .serializers import StorySerializers
# Create your views here.
class UserStory(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializers