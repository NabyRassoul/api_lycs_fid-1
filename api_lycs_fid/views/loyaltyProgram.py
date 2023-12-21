# views.py
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api_lycs_fid.models import LoyaltyProgram, LoyaltyTier
from api_lycs_fid.serializers import LoyaltyProgramSerializer, LoyaltyTierSerializer

class LoyaltyProgramDetail(generics.RetrieveUpdateAPIView):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    # permission_classes = [IsAuthenticated]
    # lookup_field = 'id'
    def get(self, request, id, format=None):
        try:
            item = LoyaltyProgram.objects.get(pk=id)
            serializer = LoyaltyProgramSerializer(item)
            return Response(serializer.data)
        except LoyaltyProgram.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
class LoyaltyTierCreate(generics.CreateAPIView):
    queryset = LoyaltyTier.objects.filter(archived=False)
    serializer_class = LoyaltyTierSerializer
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, id, format=None):
        try:
            item = LoyaltyTier.objects.filter(archived=False)
            serializer = LoyaltyTierCreate(item)
            return Response(serializer.data)
        except LoyaltyTier.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)