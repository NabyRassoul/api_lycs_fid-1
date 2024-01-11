from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions, status
from api_lycs_fid.models import User, Points
from api_lycs_fid.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404


class AttributionPointsView(generics.ListCreateAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer 

    def post(self, request, format=None):
        # Assumez que le partenaire est authentifié et a accès à la vue d'attribution des points
        partenaire = self.request.user  # Utilisez self.request.user au lieu de request.user

        # Récupérez les données du corps de la requête
        client_id = request.data.get('client_id')
        points_attribues = request.data.get('points_attribues')

        # Vérifiez si le client existe
        try:
            client = get_object_or_404(User, pk=client_id)
        except User.DoesNotExist as e:
            print(f"Client with ID {client_id} not found. Error: {e}")
            return Response({"error": f"Client with ID {client_id} not found"}, status=status.HTTP_404_NOT_FOUND)
                
        # Vérifiez si le montant des points attribués est valide
        if points_attribues is None or not isinstance(points_attribues, int):
            print('le client ', points_attribues)
            return Response({"error": "Invalid points_attribues value"}, status=status.HTTP_400_BAD_REQUEST)

        # Créez un sérialiseur Points avec les données de la requête
        serializer = PointsSerializer(data={'client': client.id, 'partner': partenaire.id, 'points': points_attribues})

        # Validez les données du sérialiseur
        if serializer.is_valid():
            # Créez un nouvel objet Points
            serializer.save()

            # Vous pouvez également renvoyer les détails de l'attribution des points si nécessaire
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # En cas d'erreurs de validation du sérialiseur
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['POST'])
# def attribuer_points_fidelite(request):
#     # Assumez que le partenaire est authentifié et a accès à la vue d'attribution des points
#     partenaire = request.user

#     # Récupérez les données du corps de la requête
#     client_id = request.data.get('client_id')
#     points_attribues = request.data.get('points_attribues')

#     # Vérifiez si le client existe
#     try:
#         client = User.objects.get(pk=client_id)
#     except User.DoesNotExist:
#         return Response({"error": f"Client with ID {client_id} not found"}, status=status.HTTP_404_NOT_FOUND)

#     # Vérifiez si le montant des points attribués est valide
#     if points_attribues is None or not isinstance(points_attribues, int):
#         return Response({"error": "Invalid points_attribues value"}, status=status.HTTP_400_BAD_REQUEST)

#     # Créez un sérialiseur Points avec les données de la requête
#     serializer = PointsSerializer(data={'client': client.id, 'partner': partenaire.id, 'points': points_attribues})

#     # Validez les données du sérialiseur
#     if serializer.is_valid():
#         # Créez un nouvel objet Points
#         serializer.save()

#         # Vous pouvez également renvoyer les détails de l'attribution des points si nécessaire
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # En cas d'erreurs de validation du sérialiseur
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # views.py
# # @api_view(['GET'])
# # def consulter_solde_points(request):
# #     client = request.user
# #     solde_points = client.points_received.aggregate(models.Sum('points'))['points__sum'] or 0
# #     details_points_par_partenaire = [
# #         {
# #             "partner_name": partner.username,  # Changez cela en champ approprié pour le nom du partenaire
# #             "points_attributed": partner.points_given.filter(client=client).aggregate(models.Sum('points'))['points__sum'] or 0
# #         }
# #         for partner in User.objects.filter(is_partner=True)
# #     ]

# #     return Response({"solde_points": solde_points, "details_points_par_partenaire": details_points_par_partenaire})
