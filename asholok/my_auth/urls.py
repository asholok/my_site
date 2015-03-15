from django.conf.urls import patterns, url
from my_auth import views

urlpatterns = patterns("", 
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^social_check/$', views.social_check, name='social_check'),
)

