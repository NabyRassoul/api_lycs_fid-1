# models.py
from django.db import models

class Points(models.Model):
    client = models.ForeignKey('api_lycs_fid.Client', on_delete=models.CASCADE, related_name='points_received')
    partner = models.ForeignKey('api_lycs_fid.Partner', on_delete=models.CASCADE, related_name='points_given')
    points = models.PositiveIntegerField()
    date_attributed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.firstName} - {self.points} points (attributed by {self.partner.name})"