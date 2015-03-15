from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns("", 
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^from/$', views.CreatePost.as_view(), name='form'),
    url(r'^article/(?P<slug>[\w-]+)/$', views.Detail.as_view(), name='detail'),
)

