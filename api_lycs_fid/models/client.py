from django.db import models
from api_lycs_fid.models import User


class Client(User):
   
    
    class Meta:
  
        db_table = "api_lycs_fid_client"
        app_label = "api_lycs_fid"

    def __str__(self):
        return f"{self.firstName}"