
from django.http import HttpResponse
from api_lycs_fid.models import Partner
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class PartnerView(TemplateView):
  template_name = "dashboard/components/partner/partners.html"

  def post(self, request):
    partner = Partner(
      firstName=request.POST['firstName'],
      lastName=request.POST['lastName'],
      email=request.POST['email'],
      adresse=request.POST['email'],
      phone=request.POST['phone'],
      name=request.POST['name'],
      contactRef=request.POST['contactRef'],
      groupe=request.POST['groupe'],
      sousGroupe=request.POST['sousGroupe'],
      ninea=request.POST['ninea'],
      
      
      
      
    )
    partner.save()
    return HttpResponseRedirect('/partners/')

  def get(self, request):
    if(request.user.is_superuser):
      partners = Partner.objects.all()
      context = {
        'currentUser': request.user,
        'partners': partners
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeletePartnerByIdView(TemplateView):
  template_name = "dashboard/components/partner/partners.html"
  def get(self, request, id, format=None):
    partner = Partner.objects.get(pk=id)
    partner.delete()
    return HttpResponseRedirect('/partners/')
