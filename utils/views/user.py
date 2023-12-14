
from django.http import HttpResponse
from api_lycs_fid.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class UserView(TemplateView):
  template_name = "dashboard/components/users/users.html"

  def post(self, request):
    user = user(
      firstName=request.POST['firstName'],
      lastName=request.POST['lastName'],
      email=request.POST['email'],
      adresse=request.POST['email'],
      phone=request.POST['phone'],
      
      
    )
    user.save()
    return HttpResponseRedirect('/users/')

  def get(self, request):
    if(request.user.is_superuser):
      users = User.objects.all()
      context = {
        'currentUser': request.user,
        'users': users
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeleteUserByIdView(TemplateView):
  template_name = "dashboard/components/users/users.html"
  def get(self, request, id, format=None):
    user = User.objects.get(pk=id)
    user.delete()
    return HttpResponseRedirect('/users/')
