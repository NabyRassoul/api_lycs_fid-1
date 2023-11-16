from api_lycs_fid.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# clients 

class CampagneAPIView(generics.CreateAPIView):
    """
    POST api/v1/campagnes/
    """
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer

    def post(self, request):
        
        serializer = CampagneSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Campagne.objects.order_by('pk')
        serializer = CampagneSerializer(items, many=True, context={'request':request})
        return Response({"count": items.count(),"data":serializer.data})


class CampagneByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer

    def get(self, request, id, format=None):
        try:
            item = Campagne.objects.get(pk=id)
            serializer = CampagneSerializer(item)
            return Response(serializer.data)
        except Campagne.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Campagne.objects.get(pk=id)
        except Campagne.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = CampagneSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, *args, **kwargs):
        try:
            item = Campagne.objects.get(id=kwargs["id"])
        except Campagne.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)