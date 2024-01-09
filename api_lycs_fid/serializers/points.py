# api_lycs_fid/serializers.py

from rest_framework import serializers
from api_lycs_fid.models import Points


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ['client', 'partner', 'points']