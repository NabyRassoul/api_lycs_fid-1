from django.db import models
from api_lycs_fids.models import User


class Client(User):
    age = models.CharField(max_length=250,blank=True)
    sexe = models.CharField(max_length=250,blank=True)
    def save(self, *args, **kwargs):
        if not self.id:
            # Si l'utilisateur est nouvellement créé, utilisez set_password pour hacher le mot de passe
            self.set_password(self.password)

        super(Client, self).save(*args, **kwargs)
    class Meta:
  
        db_table = "fid_client"
        app_label = "lycs"

    def __str__(self):
        return f"{self.firstName}"