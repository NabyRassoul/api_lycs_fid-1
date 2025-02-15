# # Create your views here.
from django.shortcuts import render
from utils.mylogForm.login_form import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.shortcuts import red
from django.shortcuts import render
from django.shortcuts import redirect


def BASE(request):
    if(request.user.is_superuser):
    
      context = {
        'currentUser': request.user,
        
      }
      return render(request, 'base.html', context)
    return render(request, 'dashboard/login.html')
    
def Tab(request):
    return render(request, 'tables.html')

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'dashboard/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username}, welcome back!')
                return redirect('')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})

# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound

# class BaseModelAPIView(generics.GenericAPIView):
#     model = None  # Assurez-vous de spécifier le modèle dans les sous-classes
#     queryset = None  # Assurez-vous de spécifier le queryset dans les sous-classes
#     serializer_class = None  # Assurez-vous de spécifier le sérialiseur dans les sous-classes

#     def get_object_or_404(self, pk):
#         try:
#             return self.queryset.filter(archived=False).get(pk=pk)
#         except self.model.DoesNotExist:
#             raise NotFound("No such item with this id")

#     def get_serializer_context(self):
#         return {'request': self.request}

# class ModelAPIView(BaseModelAPIView):
#     # permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", **serializer.data}, status=status.HTTP_201_CREATED)
#         return Response({"status": "failure", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, format=None):
#         query_params = request.query_params
#         if query_params:
#             params = {key: value for key, value in query_params.items() if hasattr(self.model, key)}
#             queryset = self.queryset.filter(archived=False).filter(**params)
#         else:
#             queryset = self.queryset.all().order_by('pk')


#         serializer = self.serializer_class(queryset, many=True, context=self.get_serializer_context())
#         return Response({"status": "success", "count": queryset.count(), "data":serializer.data}, status=status.HTTP_200_OK)

# class ModelByIdAPIView(BaseModelAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, id, format=None):
#         item = self.get_object_or_404(id)
#         serializer = self.serializer_class(item, context=self.get_serializer_context())
#         return Response({"status": "success", **serializer.data}, status=status.HTTP_200_OK)

#     def put(self, request, id, format=None):
#         item = self.get_object_or_404(id)
#         data = request.data.copy()
#         serializer = self.serializer_class(item, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success",**serializer.data}, status=status.HTTP_200_OK)
#         return Response({"status": "failure", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id, format=None):
#         item = self.get_object_or_404(id)
#         item.archived = True
#         item.save()
#         return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)