from django.db import models
from api_lycs_fid.models import User


class Partner(User):
    name = models.CharField(max_length=100, blank=True)
    groupe = models.CharField(max_length=100, blank=True)
    sousGroupe = models.CharField(max_length=100, blank=True)
    ninea  = models.CharField(max_length=100, blank=True)
    
    class Meta:
  
        db_table = "api_lycs_fid_partner"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.name}"