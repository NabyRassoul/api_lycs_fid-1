# Dans models.py de votre application
from django.db import models
from django.utils import timezone

class SignalMessage(models.Model):
    message_type = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Définir la période de rétention (par exemple, 30 jours)
        retention_period = timezone.now() - timezone.timedelta(days=1)

        # Supprimer les anciens messages
        SignalMessage.objects.filter(created_at__lt=retention_period).delete()

        super().save(*args, **kwargs)
