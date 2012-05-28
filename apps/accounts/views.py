from apps.accounts.forms import RegisterForm
from django.conf import settings
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def profile(request):
    ctx = {
        'profile':request.user.get_profile()
    }
    return render_to_response('accounts/profile.html', ctx, context_instance=RequestContext(request))

def register(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        
        login(request, user)
        
        return redirect(reverse('accounts_profile'))

    ctx = {
        'form':form
    }

    return render_to_response('accounts/register.html', ctx, context_instance=RequestContext(request))