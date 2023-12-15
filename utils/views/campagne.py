
from django.http import HttpResponse
from api_lycs_fid.models import Campagne
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class CampagneView(TemplateView):
  template_name = "dashboard/components/campagnes/campagnes.html"

  def post(self, request):
    campagne = Campagne(
        dateDebut=request.POST['dateDebut'],
        dateFin=request.POST['dateFin'],
        nomCampagne=request.POST['nomCampagne'],
        codePromo=request.POST['codePromo'],
        description=request.POST['description'],
        ageCible=request.POST['ageCible'],
        sexeCible=request.POST['sexeCible'],
        localisation=request.POST['localisation'],
        image=request.POST['image'],
        author=request.POST['author']
    )
    campagne.save()
    return HttpResponseRedirect('/campagnes/')

  def get(self, request):
    if(request.user.is_superuser):
      campagnes = Campagne.objects.all()
      context = {
        'currentUser': request.user,
        'campagnes': campagnes
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeleteCampagneByIdView(TemplateView):
  template_name = "dashboard/components/campagnes/campagnes.html"
  def get(self, request, id, format=None):
    campagne = campagne.objects.get(pk=id)
    campagne.delete()
    return HttpResponseRedirect('/campagnes/')
