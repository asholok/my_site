from django.conf.urls import patterns, url
from my_auth import views

urlpatterns = patterns("", 
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', views.Registator.as_view(), name='registration'),
    url(r'^thenx/$', views.Thx.as_view(), name='thx'),
    url(r'^social_check/$', views.social_check, name='social_check'),
    url(r'^check_email/$', views.check_email, name='check_email'),
)

