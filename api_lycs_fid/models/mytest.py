from django.db import models
from utils.models import BaseModel

class Mystest(BaseModel):
    name= models.CharField( max_length=50)

    class Meta:
        db_table = "api_lycs_fid_test"
        app_label = "api_lycs_fid"
    def __str__(self):
        return self.name

    