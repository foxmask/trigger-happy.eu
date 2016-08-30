from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# from registration.forms import RegistrationFormUniqueEmail

from th.views import TriggerHappyInfosTemplateView,\
TriggerHappyDevsTemplateView,\
TriggerHappyContactTemplateView,\
TriggerHappyHomeTemplateView,\
TriggerHappyPrivacyTemplateView,\
TriggerHappyHomeTestTemplateView

# sitemaps
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
}
# sitemaps 

urlpatterns = [

        # ****************************************
        # admin module
        # ****************************************
        url (r'^admin/', include(admin.site.urls)),
        url (r'', include('django_th.urls')),
        # url (r'^th/search', include('th_search.urls')),
        url (r'^th/holidays', include('th_holidays.urls')),

        # ****************************************
        # trigger happy module
        # ****************************************
        url (r'^infos/$', TriggerHappyInfosTemplateView.as_view(), name='infos'),
        url (r'^dev/$', TriggerHappyDevsTemplateView.as_view(), name='dev'), 
        url (r'^contactus/$', TriggerHappyContactTemplateView.as_view(), name='contactus'),
        url (r'^privacy/$', TriggerHappyPrivacyTemplateView.as_view(), name='privacy'),
        url (r'^$', TriggerHappyHomeTemplateView.as_view(), name="th_home"),

        # ****************************************
        # auth module
        # ****************************************
        # url(r'^auth/', include('django.contrib.auth.urls')),
        # ****************************************
        # allauth  module
        # ****************************************
        url(r'^accounts/', include('allauth.urls')),

        # ****************************************
        # customized lgout action
        # ****************************************
        # url(r'^logout/$', 'django_th.views.logout_view', name='logout'),
        

        # ****************************************
        # Sitemaps
        # ****************************************
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap')
]
