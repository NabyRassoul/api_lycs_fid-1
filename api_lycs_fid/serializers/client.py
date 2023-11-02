from api_lycs_fid.models import Client
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class ClientSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    class Meta:
        model = Client
        fields =('id','firstName','lastName','phone','adresse','email','user_id')
        fields = '__all__'
