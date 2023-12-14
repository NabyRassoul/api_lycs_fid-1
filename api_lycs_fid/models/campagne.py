from django.db import models
from django.utils import timezone
from .partenaire import Partner
from .user import User
from django.conf import settings

CHOIX_SEXE = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
CHOIX_AGE= (
    ('0-10 ans', '0 à 10 ans'),
    ('10-20 ans', '10 à 20 ans'),
    ('20-40 ans', '20 à 40 ans'),
    ('40-60 ans', '40 à 60 ans'),
    ('60plus', '60 ans et plus'),
)

class Campagne(models.Model):
    dateDebut = models.DateTimeField(default=timezone.now)
    dateFin = models.DateTimeField(default=timezone.now)
    nomCampagne = models.CharField(max_length=250)
    codePromo = models.CharField(max_length=250)
    ageCible = models.CharField(max_length=250,blank=True, choices=CHOIX_AGE)
    sexeCilbe = models.CharField(max_length=250,blank=True,choices=CHOIX_SEXE)
    localisation = models.CharField(max_length=250,blank=True, default='adresse')
    description = models.CharField(max_length=512, blank=True)
    image = models.ImageField(upload_to='myPucturs',null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='authorCamp')
    views = models.ManyToManyField(User,blank=True, related_name='viewsCamp')
    likes = models.ManyToManyField(User,blank=True, related_name='likesCamp')
    archived = models.BooleanField(default=False)
    
    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_lycs_fid_campagne"
        app_label = "api_lycs_fid"

    def __str__(self):
        return self.nomCampagne