from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from api_lycs_fid.models import Partner

class ConfirmEmail(APIView):
    def get(self, request, token):
        try:
            user = Partner.objects.get(confirmation_token=token)

            # Marquez l'utilisateur comme confirmé
            user.is_confimerd = True
            user.confirmation_token = None  # Effacez le jeton de confirmation
            user.save()
            print('tankyu', user)
            return redirect('login')  # Redirigez l'utilisateur vers la page de connexion
        except Partner.DoesNotExist:
            return Response({'message': 'Le lien de confirmation est invalide.'})
