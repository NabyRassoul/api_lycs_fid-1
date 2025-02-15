from api_lycs_fid.serializers import *
from api_lycs_fid.models import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# the test


from rest_framework.permissions import IsAuthenticated
class ArticleAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/Article/
    """
    
    queryset = Article.objects.filter(archived=False)
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)
    def post(self, request):
        
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(image=self.request.data.get('image'))
            serializer.save()
            
            return Response( serializer.data,status=201)
        return Response(serializer.errors, status=400)
          
    def get(self, request, format=None):
        items = Article.objects.filter(archived=False).order_by('pk')
        serializer = ArticleSerializer(items, many=True, context={'request':request})
        return Response({"count": items.count(),"data":serializer.data})

class ArticleByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Article.objects.filter(archived=False)
    serializer_class = ArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = Article.objects.filter(archived=False).get(pk=id)
            serializer = ArticleSerializer(item)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Article.objects.filter(archived=False).get(pk=id)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = ArticleSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Article.objects.filter(archived=False).get(id=kwargs["id"])
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
