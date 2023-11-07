from api_lycs_fid.models import User
# from ..models import User
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ('id','phone','lastName','firstName','password','adresse','email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # return User.objects.create(**validated_data)
        user = User(
            phone=validated_data['phone'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            adresse = validated_data['adresse']
        )
        user.user_type='owner'
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

# for upload file 
class FileUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()

