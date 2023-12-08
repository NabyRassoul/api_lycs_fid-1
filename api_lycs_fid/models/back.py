from django.db import models

class Back(models.Model):
    back= models.CharField( max_length=50)

    class Meta:
        db_table = "api_lycs_fid_back"
        app_label = "api_lycs_fid"
    def __str__(self):
        return self.back

    