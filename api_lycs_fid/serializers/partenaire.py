from api_lycs_fid.models import Partner
from ..models import*
from rest_framework import serializers
from django.contrib.auth import get_user_model

class PartnerSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    class Meta:
        model = Partner
        fields =('id','firstName','lastName','phone','adresse','email','name','groupe','sousGroupe','ninea','user_id')
        fields = '__all__'