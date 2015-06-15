from django.conf.urls import patterns, include, url
from django.contrib import admin
from my_auth.backends import PREPARED_BACKENDS
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['available_backends'] = PREPARED_BACKENDS
        
        return context

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asholok.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^convertor/', include('convertor.urls', namespace='convertor')),
    url(r'^my_auth/', include('my_auth.urls', namespace='my_auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
