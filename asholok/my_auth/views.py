from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from my_auth.models import User
from django.contrib.auth import logout as clear

def index(request):
    return HttpResponseRedirect('/')
    
def login(request):
    try:
        user = User.objects.get(user_mail=request.POST.get('email'))

        if user.password == request.POST.get('password'):
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
    # try:
    #     del request.session['user_id']
    #     del request.session['user_name']
    #     del request.session['user_mail']
    # except:
    #     pass
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
    # print request.user.email
    return HttpResponseRedirect('/')

# Create your views here.
