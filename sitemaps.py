from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from blog.apps.data.models import Entry

from datetime import datetime

class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Entry.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return '/'

class SiteSitemap(Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse(obj)
