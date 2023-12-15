from api_lycs_fid.models import Partner
from ..models import*
from rest_framework import serializers
from django.contrib.auth import get_user_model

class PartnerSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    # confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = Partner
        fields =('id','lastName','firstName','phone','adresse','email','name','groupe','sousGroupe','contactRef','ninea', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
   