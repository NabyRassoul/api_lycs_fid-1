from django.db import models
from django.utils import timezone
from .partenaire import Partner


class Article(models.Model):
    dateDebutPromo = models.DateTimeField(default=timezone.now)
    dateFinPromo = models.DateTimeField(default=timezone.now)
    nomArticle = models.CharField(max_length=250)
    reduction = models.CharField(max_length=250)
    description = models.CharField(max_length=512)
    prixDeVente = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    partnerId = models.ForeignKey(Partner,on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_lycs_fid_article"
        app_label = "api_lycs_fid"

    def __str__(self):
        return self.nomArticle
