from api_lycs_fid.models import Client
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class ClientSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    
    class Meta:
        model = Client
        fields = ('id','lastName','firstName','phone','adresse','email','sexe','age','password')
        extra_kwargs = {'password': {'write_only': True}}
   
    
    # def create(self, validated_data):
    #     # return User.objects.create(**validated_data)
    #     user = Client(
    #         phone=validated_data['phone'],
    #         firstName=validated_data['firstName'],
    #         lastName=validated_data['lastName'],
    #         email=validated_data['email'],
    #         adresse = validated_data['adresse'],
    #         age= validated_data["age"],
    #         sexe= validated_data["sexe"]
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

