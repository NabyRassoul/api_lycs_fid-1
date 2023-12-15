from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
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
    path('', views.BASE, name='BASE'),
    path('table/', views.Tab, name='Tab'),
    path('login/', views.sign_in, name='login'),
    path("articles/", views.ArticleView.as_view()),
    path("articles/delete/<int:id>/",views.DeleteArticleByIdView.as_view()),
    path("bons/", views.BonView.as_view()),
    path("bons/delete/<int:id>/",views.DeleteBonByIdView.as_view()),
    path("campagnes/", views.CampagneView.as_view()),
    path("campagnes/delete/<int:id>/",views.DeleteCampagneByIdView.as_view()),
    path("clients/", views.ClientView.as_view()),
    path("clients/delete/<int:id>/",views.DeleteClientByIdView.as_view()),  
    path("partners/", views.PartnerView.as_view()),
    path("partners/delete/<int:id>/",views.DeletePartnerByIdView.as_view()),        
    path("users/", views.UserView.as_view()),
    path("users/delete/<int:id>/",views.DeleteUserByIdView.as_view()),        


   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()



# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

# urlpatterns = [
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
# ]