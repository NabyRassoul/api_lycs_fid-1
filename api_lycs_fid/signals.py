from django.db.models.signals import post_save
import json
from django.dispatch import receiver
from django.http import HttpResponse
from api_lycs_fid.models import Article, BonReduction, Campagne, SignalMessage


@receiver(post_save, sender=Article)
def article_created(sender, instance, created, **kwargs):
    if created:
        # response_data={'message':'A new article was created:' ,'Nom':instance.nomArticle}
        SignalMessage.objects.create(message_type='Article', message=f'A new article was created: {instance.nomArticle}')
       
        # return HttpResponse(json.dumps(response_data), content_type='application/json')
        

@receiver(post_save, sender=BonReduction)
def bon_created(sender, instance, created, **kwargs):
    if created:
        print('A new bon was created:', instance.typeDeReduction, instance.codeDeReduction, instance.montantDeReduction)

@receiver(post_save, sender=Campagne)
def campagne_created(sender, instance, created, **kwargs):
    if created:
        print('A new campagne was created:', instance.nomCampagne, instance.dateDebut, instance.dateFin)
