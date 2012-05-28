from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('blog.apps.accounts.views',
    url(r'^profile/$', 'profile', name="accounts_profile"),
    url(r'^register/$', 'register', name="accounts_register"),

)

urlpatterns += patterns('',
    url(r'login/$', login, kwargs={'template_name': 'accounts/login.html'}, name="accounts_login"),
    url(r'logout/$', logout, kwargs={'next_page':'/'}, name="accounts_logout"),
)
