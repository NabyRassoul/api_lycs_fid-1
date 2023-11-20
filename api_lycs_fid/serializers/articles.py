from api_lycs_fid.models import Article 
from ..models import*
from rest_framework import serializers
from .user import UserSerializer
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer(read_only=True)
    likes = UserSerializer(many=True, read_only=True)
    views = UserSerializer(many=True, read_only=True)
    author= serializers.SerializerMethodField()
    like_count= serializers.SerializerMethodField()
    view_count= serializers.SerializerMethodField()
    # is_liked= serializers.SerializerMethodField()
    # is_viewed= serializers.SerializerMethodField()
    
   # user_id = serializers.PrimaryKeyRelatedField(queryset=Partner.objects.all(), source='partnerId') 

    class Meta:
        model = Article
        fields = ('id','nomArticle','description','prix','dateDebut','dateFin','image','views','likes','author','like_count','view_count')
        
    def get_author(self, obj):
        if obj.author is not None:
            return obj.author.firstName
        else:
        # Decide what to return or do when authorCamp is None
        # You might return a default value, raise an exception, or handle it in some other way
            return None  # or another default value or action

    
    def get_like_count(self, obj):
        return len(obj.likes.all())
    
    def get_view_count(self, obj):
        return len(obj.views.all())
    #verifier si l'utilisateur a vu ou aimer l'article
    
    # def get_is_liked(self, obj):
    #     user= self.context['request'].user
    #     return True if user in obj.likes.all() else False
    
    # def get_is_viewed(self, obj):
    #     user= self.context['request'].user
    #     return True if user in obj.views.all() else False
        
        
      
        

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['partnerId'] = 'null'  # Vous pouvez gérer la représentation ici
    #     return data