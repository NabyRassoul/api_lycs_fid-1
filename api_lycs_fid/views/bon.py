from api_lycs_fid.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# clients 

class BonReductionAPIView(generics.CreateAPIView):
    """
    POST api/v1/bon/
    """
    queryset = BonReduction.objects.all()
    serializer_class = BonReductionSerializer

    def post(self, request):
        
        serializer = BonReductionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = BonReduction.objects.order_by('pk')
        serializer = BonReductionSerializer(items, many=True, context={'request':request})
        return Response({"count": items.count(),"data":serializer.data})


class BonReductionByIdAPIView(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = BonReduction.objects.all()
    serializer_class = BonReductionSerializer

    def get(self, request, id, format=None):
        try:
            item = BonReduction.objects.get(pk=id)
            serializer = BonReductionSerializer(item)
            return Response(serializer.data)
        except BonReduction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = BonReduction.objects.get(pk=id)
        except BonReduction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = BonReductionSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, *args, **kwargs):
        try:
            item = BonReduction.objects.get(id=kwargs["id"])
        except BonReduction.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)