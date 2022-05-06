from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name",read_only=True)
    last_name = serializers.CharField(source="user.last_name",read_only=True)
    email = serializers.CharField(source="user.email",read_only=True)
    
    class Meta:
        model = Profile
        fields = ('id','user','first_name','last_name','email','gender','image','is_active','age','weight','height','amount_of_water')

