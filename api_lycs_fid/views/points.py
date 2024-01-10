from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_lycs_fid.models import User, Points
from api_lycs_fid.serializers import PointsSerializer
from django import forms
from rest_framework.decorators import api_view
class AttributionPointsForm(forms.Form):
    client_id = forms.IntegerField()
    points_attribues = forms.IntegerField()

class AttributionPointsView(APIView):
    
    def post(self, request, format=None):
        # Assumez que le partenaire est authentifié et a accès à la vue d'attribution des points
        partenaire = request.user

        # Créez un formulaire avec les données du corps de la requête
        form = AttributionPointsForm(request.data)

        # Validez le formulaire
        if form.is_valid():
            # Récupérez les données du formulaire
            client_id = form.cleaned_data['client_id']
            points_attribues = form.cleaned_data['points_attribues']

            # Vérifiez si le client existe
            try:
                client = User.objects.get(pk=client_id)
            except User.DoesNotExist:
                return Response({"error": f"Client with ID {client_id} not found"}, status=status.HTTP_404_NOT_FOUND)

            # Vérifiez si le montant des points attribués est valide
            if points_attribues is None or not isinstance(points_attribues, int):
                return Response({"error": "Invalid points_attribues value"}, status=status.HTTP_400_BAD_REQUEST)

            # Créez un sérialiseur Points avec les données récupérées
            serializer = PointsSerializer(data={'client': client.id, 'partner': partenaire.id, 'points': points_attribues})

            # Validez les données du sérialiseur
            if serializer.is_valid():
                # Créez un nouvel objet Points
                serializer.save()

                # Vous pouvez également renvoyer les détails de l'attribution des points si nécessaire
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # En cas d'erreurs de validation du sérialiseur
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # En cas de formulaire non valide
        return Response({"error": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)


