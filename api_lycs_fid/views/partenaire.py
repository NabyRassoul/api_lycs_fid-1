from api_lycs_fid.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
import io, csv, pandas as pd
from ..models import Partner
import uuid
from django.core.mail import EmailMessage
from django.utils.html import format_html
from django.core.mail import send_mail
from lycsfid.settings import EMAIL_HOST_USER
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Partners 

class PartnerUploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['csv_file']
        reader = pd.read_csv(csv_file, encoding = "utf-8",error_bad_lines=False)
        for _, row in reader.iterrows():
            new_file = Partner(
                firstName= row["firstName"],
                lastName= row['lastName'],
                telephone= row["phone"],
                adresse= row["adresse"],
                email= row["email"],
                groupe= row["groupe"],
                name= row["name"],
                sousGroupe= ["sousGroupe"],
                ninea= ["ninea"],
                contactRef= ["contactRef"],
                user_id = user
                )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

def PartnerExportFileView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Partners.csv"'},
    )

    writer = csv.writer(response)
    row =["firstName","lastName","phone","adresse","email","groupe","sousGroupe","name","ninea"]
    writer.writerow(row)
    for partner in Partner.objects:

        row =[
            partner.firstName,
            partner.lastName,
            partner.phone,
            partner.adresse,
            partner.email,
            partner.contactRef,
            partner.groupe,
            partner.ninea,
            partner.sousGroupe,
            partner.name
        ]
        writer.writerow(row)

    return response

class PartnerAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/partenaires/
    """
    
    queryset= Partner.objects.filter(archived=False)
    serializer_class = PartnerSerializer

    def post(self, request, format=None):
        serializer = PartnerSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            subject = 'Confirmation de votre inscription'
            message = f"Bienvenue chez nous {user.firstName} {user.lastName} Votre inscription est en attente de validation"

            # EMAIL MESSAGE
            recipient_list = [user.email]
            from_email = 'mouhamed.ba@agencelycs.com'
            email = EmailMessage(subject, message, from_email, recipient_list)
            email.content_subtype = "html" 
            email.send()
            

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Partner.objects.filter(archived=False)
        serializer = PartnerSerializer(items, many=True)
        return Response({"count": items.count(),"data":serializer.data})



class PartnerByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Partner.objects.filter(archived=False)
    serializer_class = PartnerSerializer
    

    def get(self, request, id, format=None):
        try:
            item = Partner.objects.get(pk=id)
            serializer = PartnerSerializer(item)
            return Response(serializer.data)
        except Partner.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
            
    def put(self, request, id, format=None):
        try:
            item = Partner.objects.filter(archived=False).get(pk=id)
        except Partner.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = PartnerSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

            # return Response(serializer.errors, status=400)
    # def delete(self, request, id, format=None):
    def delete(self, request, *args, **kwargs):
        try:
            item = Partner.objects.filter(archived=False).get(id=kwargs["id"])
        except Partner.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)


class PartnerByUser(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    # permission_classes = []

    def get(self, request, id, format=None):
        try:
            item = Partner.objects.filter(createdBy=id)
        
            serializer = PartnerSerializer(item,many=True)
            return Response(serializer.data)
        except Partner.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
class ComptIsActivate(generics.RetrieveAPIView):
    queryset= Partner.objects.all()
    serializer_class = PartnerSerializer
    def get(self, request, id, format=None):
        try:
            partner = Partner.objects.filter(archived=False).get(pk=id)
            partner.is_active = True
            partner.save()
           
    # Envoyez un deuxième e-mail si is_active est maintenant True
            subject = 'Confirmation du compte actif'
            message = f"Votre compte chez nous {partner.firstName} {partner.lastName} est maintenant actif. Merci de votre inscription.http://127.0.0.1:8000/"
            recipient_list = [partner.email]
            from_email = 'mouhamed.ba@agencelycs.com'
            email = EmailMessage(subject, message, from_email, recipient_list)
            email.content_subtype = "html" 
            email.send()

            return Response({'message':message})

        except Partner.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "No such item with this id",
            }, status=404)
