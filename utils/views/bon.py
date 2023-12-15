
from django.http import HttpResponse
from api_lycs_fid.models import BonReduction
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class BonView(TemplateView):
  template_name = "dashboard/components/bon/bons.html"

  def post(self, request):
    bon = BonReduction(
      dateDebut=request.POST['dateDebut'],
      dateFin=request.POST['dateFin'],
      typeDeReduction=request.POST['typeDeReduction'],
      codeDeReduction=request.POST['codeDeReduction'],
      montantDeReduction=request.POST['montantDeReduction'],
      quantityBon=request.POST['quantityBon'],
      ageCible=request.POST['ageCible'],
      sexeCible=request.POST['sexeCible'],
      localisation=request.POST['localisation'],
      image=request.POST['image'],
      author=request.POST['author']
      
    )
    bon.save()
    return HttpResponseRedirect('/bons/')

  def get(self, request):
    if(request.user.is_superuser):
      bons = BonReduction.objects.all()
      context = {
        'currentUser': request.user,
        'bons': bons
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeleteBonByIdView(TemplateView):
  template_name = "dashboard/components/bon/bon.html"
  def get(self, request, id, format=None):
    bon = BonReduction.objects.get(pk=id)
    bon.delete()
    return HttpResponseRedirect('/bons/')
