# Dans views.py de votre application DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from api_lycs_fid.models import SignalMessage
from api_lycs_fid.serializers import SignalMessageSerializer
from rest_framework.permissions import IsAuthenticated
class SignalMessageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # Récupérer tous les messages de la base de données
        messages = SignalMessage.objects.all()
        serializer = SignalMessageSerializer(messages, many=True)
        return Response(serializer.data)
