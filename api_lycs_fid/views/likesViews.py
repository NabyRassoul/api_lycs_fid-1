from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api_lycs_fid.models import Campagne
from api_lycs_fid.serializers import *

# Dans votre_app/views.py

class LikeView(generics.CreateAPIView):
    queryset = Campagne.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        campagne = self.get_object()
        user = self.request.user
        campagne.likes.add(user)
        serializer.save()

class ViewView(generics.CreateAPIView):
    queryset = Campagne.objects.all()
    serializer_class = ViewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        campagne = self.get_object()
        user = self.request.user
        campagne.views.add(user)
        serializer.save()
