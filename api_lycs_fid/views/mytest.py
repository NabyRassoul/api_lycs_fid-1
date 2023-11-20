from utils.views import ModelByIdAPIView,ModelAPIView
from api_lycs_fid.models import *
from rest_framework import generics
from api_lycs_fid.serializers import MytestSerializer
class MytestViews(ModelAPIView):
    model= Mystest
    queryset= model.objects.filter(archived=False)
    serializer_class= MytestSerializer
    
class MytestUpdateViews(ModelByIdAPIView):
    model= Mystest
    queryset= model.objects.filter(archived=False)
    serializer_class= MytestSerializer
    
