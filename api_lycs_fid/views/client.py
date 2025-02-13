from api_lycs_fid.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from ..models import Client
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser
from api_lycs_fid.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# clients 

class ClientUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        reader = pd.read_csv(csv_file, encoding = "utf-8",error_bad_lines=False)
        for _, row in reader.iterrows():
            new_file = Client(
                firstName= row["firstName"],
                lastName= row['lastName'],
                telephone= row["phone"],
                adresse= row["adresse"],
                email= row["email"],
                age= row["age"],
                sexe= row["sexe"],
                user_id = user
                )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

def ClientExportFileView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="clients.csv"'},
    )

    writer = csv.writer(response)
    row =["firstName","lastName","phone","adresse","email",'age','sexe']
    writer.writerow(row)
    for client in Client.objects:

        row =[
            client.firstName,
            client.lastName,
            client.phone,
            client.adresse,
            client.email,
            client.age,
            client.sexe
        ]
        writer.writerow(row)

    return response

class ClientAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/client/
    """
    queryset = Client.objects.filter(archived=False)
    serializer_class = ClientSerializer

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Client.objects.filter(archived=False)
        serializer = ClientSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})

    #Attributions des points

@api_view(['GET'])
def consulter_solde_points(request):
    client = request.user
    solde_points = client.points_received.aggregate(models.Sum('points'))['points__sum'] or 0
    details_points_par_partenaire = [
        {
            "partner_name": partner.name,
            "points_attributed": partner.points_set.filter(client=client).aggregate(models.Sum('points'))['points__sum'] or 0
        }
        for partner in Partner.objects.all()
    ]

    return Response({"solde_points": solde_points, "details_points_par_partenaire": details_points_par_partenaire})

class ClientByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Client.objects.filter(archived=False)
    serializer_class = ClientSerializer

    def get(self, request, id, format=None):
        try:
            item = Client.objects.get(pk=id)
            serializer = ClientSerializer(item)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Client.objects.filter(archived=False).get(pk=id)
        except Client.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = ClientSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Client.objects.filter(archived=False).get(id=kwargs["id"])
        except Client.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)


class ClientByUser(generics.RetrieveAPIView):
    queryset = Client.objects.filter(archived=False)
    serializer_class = ClientSerializer
    # permission_classes = []

    def get(self, request, id, format=None):
        try:
            item = Client.objects.filter(createdBy=id)
        
            serializer = ClientSerializer(item,many=True)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
