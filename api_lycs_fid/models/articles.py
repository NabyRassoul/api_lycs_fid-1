from django.db import models
from django.utils import timezone
from .user import User


class Article(models.Model):
    dateDebut = models.DateTimeField(default=timezone.now)
    dateFin = models.DateTimeField(default=timezone.now)
    nomArticle = models.CharField(max_length=250)
    description = models.CharField(max_length=512, blank=True)
    prix = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='author')
    views = models.ManyToManyField(User,blank=True, related_name='views')
    likes = models.ManyToManyField(User,blank=True, related_name='likes')
    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "api_lycs_fid_article"
        app_label = "api_lycs_fid"

    def __str__(self):
        return self.nomArticle
