# # models.py

# from django.db import models
# from api_lycs_fid.models import Client

# class Points(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     points = models.PositiveIntegerField()
#     date_attributed = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.client.firstName} - {self.points} points"
