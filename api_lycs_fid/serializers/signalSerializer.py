from api_lycs_fid.models import SignalMessage
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class SignalMessageSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    
    class Meta:
        model = SignalMessage
        fields = ('id','message_type','message','created_at')
      
      