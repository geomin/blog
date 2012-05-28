from django.conf.urls.defaults import *

from blog.apps.homepage.feeds import ArchiveFeed

urlpatterns = patterns('blog.apps.homepage.views',

 url(r'^$', 'index', name="homepage_index"),
 url(r'^contact/$', 'contact', name="homepage_contact"),
 url(r'^archive/$', 'archive', name="homepage_archive"),

)

urlpatterns += patterns('',
 url(r'^about/$', 'django.contrib.flatpages.views.flatpage', kwargs={'url':'/about/'},  name="homepage_about"),
 (r'^feed/archive/$', ArchiveFeed()),
)
