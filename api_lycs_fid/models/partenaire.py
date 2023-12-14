from django.db import models
from api_lycs_fid.models import User


class Partner(User):
    name = models.CharField(max_length=100, blank=True)
    contactRef = models.CharField(max_length=100, blank=True)
    groupe = models.CharField(max_length=100, blank=True)
    sousGroupe = models.CharField(max_length=100, blank=True)
    ninea  = models.CharField(max_length=100, blank=True)
    archived = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    # confirmation_token = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # user.is_active=False
        if not self.id:
            # Si l'utilisateur est nouvellement créé, utilisez set_password pour hacher le mot de passe
            self.set_password(self.password)
            # self.is_active = False

        super(Partner, self).save(*args, **kwargs)
    
        
    
    class Meta:
  
        db_table = "api_lycs_fid_partner"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.name}"