# from django.contrib.auth.models import User
# from api_lycs_fid.models import *   # Assurez-vous d'importer correctement votre modèle UserProfile s'il existe

# def get_user_registration_token(user):
#     # Supposons que UserProfile soit un modèle qui stocke les tokens d'enregistrement FCM pour les utilisateurs
#     try:
#         # Récupérez le profil de l'utilisateur
#         user_profile = Client.objects.get(user=user)

#         # Récupérez le token d'enregistrement FCM associé à cet utilisateur
#         registration_token = user_profile.fcm_registration_token

#         return registration_token
#     except Client.DoesNotExist:
#         # Gérez le cas où le profil de l'utilisateur n'existe pas ou ne contient pas de token FCM
#         return None
