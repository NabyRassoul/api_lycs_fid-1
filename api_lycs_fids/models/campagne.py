from django.db import models
from django.utils import timezone
from .partenaire import Partner
from .user import User


class Campagne(models.Model):
    dateDebut = models.DateTimeField(default=timezone.now)
    dateFin = models.DateTimeField(default=timezone.now)
    nomCampagne = models.CharField(max_length=250)
    ageCible = models.CharField(max_length=250,blank=True)
    sexeCilbe = models.CharField(max_length=250,blank=True)
    adresse = models.CharField(max_length=250,blank=True)
    description = models.CharField(max_length=512, blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='authorCamp')
    views = models.ManyToManyField(User,blank=True, related_name='viewsCamp')
    likes = models.ManyToManyField(User,blank=True, related_name='likesCamp')
    
    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "fid_ampagne"
        app_label = "lycs"

    def __str__(self):
        return self.nomCampagne
