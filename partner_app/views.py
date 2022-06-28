from django.shortcuts import render
from rest_framework import status, viewsets
from .models import Partner
from .serializers import StorySerializers
# Create your views here.
class UserPartner(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializers