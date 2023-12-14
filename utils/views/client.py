
from django.http import HttpResponse
from api_lycs_fid.models import Client
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class ClientView(TemplateView):
  template_name = "dashboard/components/client/clients.html"

  def post(self, request):
    client = Client(
      firstName=request.POST['firstName'],
      lastName=request.POST['lastName'],
      email=request.POST['email'],
      adresse=request.POST['email'],
      phone=request.POST['phone'],
      age=request.POST['age'],
      sexe=request.POST['sexe']
      
    )
    client.save()
    return HttpResponseRedirect('/clients/')

  def get(self, request):
    if(request.user.is_superuser):
      clients = Client.objects.all()
      context = {
        'currentUser': request.user,
        'clients': clients
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeleteClientByIdView(TemplateView):
  template_name = "dashboard/components/client/clients.html"
  def get(self, request, id, format=None):
    client = Client.objects.get(pk=id)
    client.delete()
    return HttpResponseRedirect('/clients/')
