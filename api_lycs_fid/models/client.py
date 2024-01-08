from django.db import models
# from fcm_django.models import FCMDevice
from api_lycs_fid.models import *
from api_lycs_fid.models import User

CHOIX_SEXE = (
    ('M', 'Masculin'),
    ('F', 'Féminin'),
)

CHOIX_AGE = (
    ('ADULTE', 'Adulte'),
    ('ENFANT', 'Enfant')
)

class Client(User):
    age = models.CharField(max_length=250, blank=True, choices=CHOIX_AGE)
    sexe = models.CharField(max_length=250, blank=True, choices=CHOIX_SEXE)
    archived = models.BooleanField(default=False)

    # Relation avec FCMDevice
    # user_fcmdevice = models.OneToOneField(FCMDevice, on_delete=models.CASCADE, null=True, blank=True)
    
    # def solde_points_fidelite(self):
    #     return Points.objects.filter(client=self).aggregate(models.Sum('points'))['points__sum'] or 0
    def save(self, *args, **kwargs):
        if not self.id:
            # Si l'utilisateur est nouvellement créé, utilisez set_password pour hacher le mot de passe
            self.set_password(self.password)

            # # Créez un FCMDevice lors de la création de l'utilisateur
            # fcm_device = FCMDevice.objects.create(user=self, registration_id="")  # Vous devez définir le bon registration_id
            # self.user_fcmdevice = fcm_device

        super(Client, self).save(*args, **kwargs)

    class Meta:
        db_table = "api_lycs_fid_client"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.firstName}"
