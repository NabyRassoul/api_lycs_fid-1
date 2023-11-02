from api_lycs_fid.models import Article
from ..models import*
from rest_framework import serializers
from .partenaire import PartnerSerializer
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    partnerId = PartnerSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Partner.objects.all(), source='partnerId') 

    class Meta:
        model = Article
        fields =('id','dateDebutPromo','dateFinPromo','nomArticle','reduction','partnerId','description','prixDeVente','image','user_id')
        fields = '__all__'
        

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['partnerId'] = 'null'  # Vous pouvez gérer la représentation ici
    #     return data
