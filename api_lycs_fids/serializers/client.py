from api_lycs_fids.models import Client
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class ClientSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    class Meta:
        model = Client
        fields = ('id','phone','lastName','firstName','password','adresse','email','sexe','age')
        extra_kwargs = {'password': {'write_only': True}}

        
