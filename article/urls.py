from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','article.views.articles'),
    url(r'^all/(?P<article_id>\d+)/$','article.views.article'),
    url(r'^create/$','article.views.create'),
    url(r'^likes/(?P<article_id>\d+)/$','article.views.likes_inc'),
)
