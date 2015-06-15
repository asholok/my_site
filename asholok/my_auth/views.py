import hashlib
from form import CaptchaModelForm
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout as clear
from my_auth.models import User
from my_auth.backends import PREPARED_BACKENDS

def index(request):
    return HttpResponseRedirect('/')
    
def login(request):
    try:
        user = User.objects.get(user_mail=request.POST.get('email'))
        md5_pass = hashlib.md5(request.POST.get('password')).hexdigest()

        if user.password == md5_pass:
            request.user = user
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session['user_mail'] = user.user_mail
        else:
            messages.error(request, 'Wrong email or password!')
    except User.DoesNotExist:
        messages.error(request, 'Wrong email or password!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def logout(request):
    clear(request)
    return HttpResponseRedirect('/')

def social_check(request):
    # specifier = request.user.social_auth.values_list('provider')[0][0]
    try:
        user = User.objects.get(user_mail=request.user.email)

        request.session['user_id'] = user.id
        request.session['user_name'] = user.username
        request.session['user_mail'] = user.user_mail
    except User.DoesNotExist:
        pass
    return HttpResponseRedirect('/')

def check_email(request):
    if request.method == 'GET':
        dict_GET = request.GET.copy()
        if dict_GET.has_key('user_mail'):
            if User.objects.filter(user_mail=request.GET['user_mail']):
                return HttpResponse(False)
            
            return HttpResponse(True)

    return HttpResponseRedirect('/')


class Registator(generic.CreateView):
    model = User
    form_class = CaptchaModelForm
    template_name = 'registration/registration.html'
    
    def get_success_url(self):
        return reverse('my_auth:thx')

    def get_context_data(self, **kwargs):
        context = super(Registator, self).get_context_data(**kwargs)
        context['action'] = reverse('my_auth:registration')
        context['available_backends'] = PREPARED_BACKENDS

        return context

class Thx(generic.TemplateView):
    template_name = 'registration/thx.html'

    def get_context_data(self, **kwargs):
        context = super(Thx, self).get_context_data(**kwargs)
        context['available_backends'] = PREPARED_BACKENDS

        return context
