from django.db import models
# from django.contrib.auth.models import User
from api_lycs_fid.models import User

class LoyaltyTier(models.Model):
    #Montant nécessaire pour atteindre ce palier
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    # Nombre de points attribués pour atteindre ce palier
    equiPoints = models.IntegerField()
    
    # Récompense associée à ce palier
    
    archived = models.BooleanField(default=False)
    class Meta:

        db_table = "api_lycs_fid_Paliers"
        app_label = "api_lycs_fid"
    def __str__(self):
        return f"Montant nécessaire - {self.montant} Fcfa "

class LoyaltyProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tiers = models.ManyToManyField(LoyaltyTier)
    
    class Meta:
        db_table = "api_lycs_fid_loyaltyProgram"
        app_label = "api_lycs_fid"
    
    def __str__(self):
        return f"Dans le progrm - {self.user.firstName} - {self.user.lastName}"
