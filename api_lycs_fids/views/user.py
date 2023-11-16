# from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from api_lycs_fids.serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import action




# list user 
class UserAPIView(generics.CreateAPIView):
    """
    GET api/v1/users/
    POST api/v1/users/
    """
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.all().order_by('-id')
        if not user:
            return Response({
                "status": "failure",
                "message": "no such item",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, many=True)

        return Response({
            "status": "success",
            "message": "user successfully retrieved.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        #user = request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            #je vais mettre mon email de notification
            serializer.save()
            return Response( serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
        

class UserById(generics.UpdateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404) 
        serializer = UserSerializer(item, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class UserUpdatePassword(generics.UpdateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, format=None):
        try:
            email = request.data['email']
            item = User.objects.get(email=email)
            password = request.data['password']
            item.set_password(password)
            item.save()
            serializer = UserSerializer(item)
        except User.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this phone",
                }, status=404) 
        return Response(serializer.data, status=200)
