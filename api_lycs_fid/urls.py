from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from .views.partenaire import *
from .views.user import *
from .views.articles import *
from .views.auth import *
from .views.client import *
# from .views.view import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Lycs Fid",
      default_version='v1',
      description="Vue des Api Lycs_fid",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # authentification 
    path('login/', views.LoginView.as_view()),
    
    # path('partners/login/', views.PartnerLoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view()),
    path('csrftoken', views.GetCSRFToken.as_view()),

    # path('reset-password/verify-token/', views.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # # user 
    path('users/', views.UserAPIView.as_view()),
    path('users/<int:id>', views.UserById.as_view()),
    path('users/password/<int:id>', views.UserUpdatePassword.as_view()),
    

    # # clients 

    path('clients',views.ClientAPIView.as_view()),
    path('clients/upload',views.ClientUploadFileView.as_view()),
    path('clients/export',views.ClientExportFileView),
    path('clients/<int:id>/',views.ClientByIdAPIView.as_view()),
    path('clients/user/<int:id>/',views.ClientByUser.as_view()),
    #pontfidel
    path('attribuer-points/', views.AttributionPointsView.as_view()),
    # path('consulter_solde_points', views.consulter_solde_points, name='consulter_solde_points'),
    path('consulter-solde-points/', views.consulter_solde_points, name='consulter_solde_points'),
    
    
    # #Parteniare
    path('partenaires',views.PartnerAPIView.as_view()),
    path('partenaires/upload',views.PartnerUploadFileView.as_view()),
    path('partenaires/export',views.PartnerExportFileView),
    path('partenaires/<int:id>/',views.PartnerByIdAPIView.as_view()),
    path('partenaires/user/<int:id>/',views.PartnerByUser.as_view()),
    path('partenaires/active/<int:id>/',views.ComptIsActivate.as_view()),
    


    # Articles
    path('articles/',views.ArticleAPIView.as_view()),
    path('articles/<int:id>/',views.ArticleByIdAPIView.as_view()),
    # path('articles/user/<int:id>/',views.ArticleByUser.as_view()),

      #Campagne
    path('campagnes/',views.CampagneAPIView.as_view()),
    path('campagnes/<int:id>/',views.CampagneByIdAPIView.as_view()),
    path('campagnes/<int:pk>/like/', views.LikeView.as_view(), name='campagne-like'),
    path('campagnes/<int:pk>/view/', views.ViewView.as_view(), name='campagne-view'),
    
    #Bon de Reduction
    path('bon/',views.BonReductionAPIView.as_view()),
    path('bon/<int:id>/',views.BonReductionByIdAPIView.as_view()),
    path('signal-messages/', views.SignalMessageView.as_view(), name='signal-messages'),
    path('program-fidelite/<int:id>/', views.LoyaltyProgramDetail.as_view(), name='program-fidelite-detail'),
    path('program-fidelite', views.LoyaltyTierCreate.as_view(), name='program-fidelite'),
    # path('notifications/', include('notifications.urls')), # new
    # path('index/', index, name='index'),
    # path('mytest/',views.MytestViews.as_view()), 
    # path('mytest/<int:id>/',views.ModelByIdAPIView.as_view()),
    
    #parametre
    # path('parametres/', views.ParametreList.as_view()),
    # path('parametres/user/<int:id>/', views.ParametreByUser.as_view()),
    # path('profiles/<int:id>/', views.CompanyByIdAPIView.as_view()),

    # path('envoyer-message/', SendTwilioMessageView.as_view(), name='envoyer-message'),
    

    
    
    

       
    
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    urlpatterns += staticfiles_urlpatterns()

# urlpatterns = [
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
# ]