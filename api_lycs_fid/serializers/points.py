# api_lycs_fid/serializers.py

from rest_framework import serializers
from api_lycs_fid.models import Points



class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ['id', 'client', 'partner', 'points', 'date_attributed','client_name','partner_name']

    # Ajouter ces lignes pour afficher le nom du client et du partenaire dans la représentation JSON
    client_name = serializers.SerializerMethodField()
    partner_name = serializers.SerializerMethodField()

    def get_client_name(self, obj):
        return obj.client.firstName  # Remplacez par le champ correct si nécessaire

    def get_partner_name(self, obj):
        return obj.partner.name