from api_lycs_fid.models import Mystest
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class MytestSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    class Meta:
        model = Mystest
        fields = '__all__'
        
    
    
    