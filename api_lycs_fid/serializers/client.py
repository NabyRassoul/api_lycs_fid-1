from api_lycs_fid.models import Client
from ..models import*

from rest_framework import serializers
from django.contrib.auth import get_user_model

class ClientSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    
    class Meta:
        model = Client
        fields = ('id','phone','lastName','firstName','password','adresse','email','sexe','age')
        extra_kwargs = {'password': {'write_only': True}}
   
    
        def create(self, validated_data):
            # return User.objects.create(**validated_data)
            user = Client(
                phone=validated_data['phone'],
                firstName=validated_data['firstName'],
                lastName=validated_data['lastName'],
                email=validated_data['email'],
                adresse = validated_data['adresse']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email', 'password')

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

# for upload file 
class FileUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
