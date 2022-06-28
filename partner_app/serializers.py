from rest_framework import serializers
from .models import Partner

class PartnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('name','title')