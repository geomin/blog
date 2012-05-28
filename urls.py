from django.conf.urls.defaults import *

from blog import settings
from sitemaps import BlogSitemap, SiteSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
 'blog':BlogSitemap,
 'pages':SiteSitemap(['homepage_contact', 'homepage_archive'])
}

urlpatterns = patterns('',
    (r'^', include('blog.apps.homepage.urls')),
    (r'^', include('blog.apps.accounts.urls')),
    (r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    # Example:
    # (r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )
