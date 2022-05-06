from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework.response import Response
# Create your views here.

class Profiles(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(request,self):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    