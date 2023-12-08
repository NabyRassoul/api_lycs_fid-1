# script principal
import django
django.setup()
from rest_framework import generics, permissions, status
from api_lycs_fid.serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from api_lycs_fid.models import User ,Partner
from rest_framework.views import APIView
# from django.contrib.auth.backends import ModelBackend

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



class LoginView(generics.CreateAPIView):
    """
    POST api/v1/login/
    """
    queryset = User.objects.all()
    # queryset= Partner.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]
        is_active = request.data.get('is_active',True)
        if not password or not email:
            return Response(data={"message": "Both identifiant email and password are required to connect"},status=400)
        else:
            try:
                
                user = authenticate(request, email=email, password=password)
                print("voici mon user", user)
                if user is not None:
                    
                    login(request, user)
                    
                    # Redirect to a success page.
                    if user.is_active and is_active:
                        print('Is_active est a: ',is_active)
                        serializer = TokenSerializer(data={"token": jwt_encode_handler(jwt_payload_handler(user))})
                        if serializer.is_valid():
                            token = serializer.data
                            response_data = {
                                'id': user.id,
                                'token': token,
                                'phone': user.phone,
                                'firstName': user.firstName,
                                'lastName': user.lastName,
                                'email':user.email,
                                # 'user_type':user.user_type,
                            }
                            return Response(response_data) 
                    else:
                        return Response({"message": "Utilisateur non actif"}, status=400)  
                else:
                    return Response(data={"message": "Votre email ou mot de passe est incorrect , ou Utilisateur non actif"},status=401)
            except User.DoesNotExist:
                return Response(data={"message": "Cet utilisateur n'existe pas"},status=401)
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    def get(self, request, format=None):
        print(request.META['CSRF_COOKIE'])
        return Response({ 'success': 'CSRF cookie set',"csrftoken":request.META['CSRF_COOKIE'] })
        
class LogoutView(APIView):
  def get(self, request):
      logout(request)
      return Response({ 'success': "logged out"})


# class EmailOrUsernameModelBackend(ModelBackend):
#     """
#     Auth backend that allows authentication with either email or username.
#     """
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             try:
#                 user = Partner.objects.get(email=email)
#             except Partner.DoesNotExist:
#                 return None
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
#         return None

