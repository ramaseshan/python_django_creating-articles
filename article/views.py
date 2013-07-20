# Create your views here.
from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import ArticleForm
from django.http import HttpResponse


def articles(request):
    return render_to_response('articles.html',
                              {'articles':Article.objects.all()})
def article(request, article_id):
    return render_to_response('article.html',
                              {'article':Article.objects.get(id=article_id)})

def create(request):
    if request.POST:
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/articles/all/')
    else:
        form = ArticleForm()
        
    args={}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html',args)

def likes_inc(request,article_id):
    
    if article_id:
        a=Article.objects.get(id=article_id)
        count = a.likes
        count+=1
        a.likes=count
        a.save()
        
    return HttpResponseRedirect('/articles/all/%s' % article_id)