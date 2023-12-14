from django.db import models
from api_lycs_fid.models import User
CHOIX_SEXE = (
         ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
CHOIX_AGE= (
    ('ADULTE','Adulte'),
    ('ENFANT','Enfant')
)
class Client(User):
    age = models.CharField(max_length=250,blank=True, choices=CHOIX_AGE)
    sexe = models.CharField(max_length=250,blank=True, choices=CHOIX_SEXE)
    archived = models.BooleanField(default=False)
   
    def save(self, *args, **kwargs):
        if not self.id:
            # Si l'utilisateur est nouvellement créé, utilisez set_password pour hacher le mot de passe
            self.set_password(self.password)

        super(Client, self).save(*args, **kwargs)
    class Meta:
  
        db_table = "api_lycs_fid_client"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.firstName}"