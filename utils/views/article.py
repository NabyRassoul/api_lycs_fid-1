
from django.http import HttpResponse
from api_lycs_fid.models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

class ArticleView(TemplateView):
  template_name = "dashboard/components/articles/articles.html"

  def post(self, request):
    article = Article(
      nomArticle=request.POST['nomArticle'],
      ageCible=request.POST['ageCible'],
      sexeCible=request.POST['sexeCible'],
      author=request.POST['author']
    )
    article.save()
    return HttpResponseRedirect('/articles/')

  def get(self, request):
    if(request.user.is_superuser):
      articles = Article.objects.all()
      context = {
        'currentUser': request.user,
        'articles': articles
      }
      return render(request, self.template_name,context)
    return render(request, 'dashboard/login.html')

class DeleteArticleByIdView(TemplateView):
  template_name = "dashboard/components/article/article.html"
  def get(self, request, id, format=None):
    article = Article.objects.get(pk=id)
    article.delete()
    return HttpResponseRedirect('/articles/')
