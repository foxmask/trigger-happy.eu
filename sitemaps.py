from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['th_home', 'infos', 'dev', 'contactus']

    def location(self, item):
        return reverse(item)

