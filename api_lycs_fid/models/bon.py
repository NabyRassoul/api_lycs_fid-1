from django.db import models
from django.utils import timezone
from .user import User
CHOIX_SEXE = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
CHOIX_AGE= (
    ('Adulte','Adulte'),
    ('Enfant','Enfant')
)

class BonReduction(models.Model):
    
    dateDebut = models.DateTimeField(default=timezone.now)
    dateFin = models.DateTimeField(default=timezone.now)
    typeDeReduction = models.CharField(max_length=250)
    codeDeReduction = models.CharField(max_length=512, blank=True)
    montantDeReduction = models.IntegerField()
    quantityBon = models.IntegerField()
    ageCible = models.CharField(max_length=50,blank=True, choices=CHOIX_AGE)
    sexeCible = models.CharField(max_length=250,blank=True, choices=CHOIX_SEXE)
    localisation = models.CharField(max_length=250,blank=True,default='adresse')
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='authorBon')
    views = models.ManyToManyField(User,blank=True, related_name='viewsBon')
    likes = models.ManyToManyField(User,blank=True, related_name='likesBon')
    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_lycs_fid_bonReduction"
        app_label = "api_lycs_fid"

    def __str__(self):
        return self.typeDeReduction