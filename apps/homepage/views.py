from django.db.models.aggregates import Count, Avg, Min, Max
from django.shortcuts import render_to_response
from blog.apps.data.models import Entry
from django.template import RequestContext
from django.db import backend, connections
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import send_mail, mail_admins

from blog.apps.homepage.forms import ContactForm
from blog.apps.homepage import signals

def index(request):
    entries = Entry.objects.published_entries().order_by('-id')

    paginator = Paginator(entries, 2)

    page_num = request.GET.get('page', 1)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)

    ctx = {
        'page':page
    }
    return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
    return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):

    success = False
    email = ""
    title = ""
    text = ""
    contact_sent = request.session.get('contact_sent', False)

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            print "WORKED"
        else:
            print "DOES NOT WORK"

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']

            request.session["contact_sent"] = True

            #send_mail("Your subject\nsaas", "Your text message! Data sent: %s %s %s\nsdsd" % (title,text,email), 'mail.from@serversdsds.com\n', ['user.to@youremailservererwerefsef.com\n'], fail_silently=False)
            #mail_admins("other subject", "some text", fail_silently=False)

            signals.message_sent.send(sender=ContactForm, email=email)
    else:
        contact_form = ContactForm()

    ctx = {'contact_form':contact_form, 'contact_sent':contact_sent, 'email':email, 'title':title, 'text':text, 'success':success}

    request.session.set_test_cookie()

    return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

def archive(request):

    base_qs = Entry.objects.filter(published=True)

    in_archive = base_qs.aggregate(count=Count('pk'), max=Max('pk'), min=Min('pk'), avg=Avg('pk'))

    month = backend.DatabaseOperations(connections).date_trunc_sql('month', 'created')
    per_month_count = base_qs.extra({'date':month}).values('date').annotate(count=Count('pk')).order_by('date')

    ctx = {
        'in_archive':in_archive,
        'per_month_count':per_month_count
    }

    return render_to_response('homepage/archive.html', ctx, context_instance=RequestContext(request))

