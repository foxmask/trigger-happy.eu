from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

# from registration.forms import RegistrationFormUniqueEmail

from th.views import TriggerHappyInfosTemplateView,\
TriggerHappyDevsTemplateView,\
TriggerHappyContactTemplateView,\
TriggerHappyHomeTemplateView,\
TriggerHappyHomeTestTemplateView

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
        url (r'^infos/$', TriggerHappyInfosTemplateView.as_view()),
        url (r'^dev/$',   TriggerHappyDevsTemplateView.as_view()),
        url (r'^contactus/$', TriggerHappyContactTemplateView.as_view()),
        url (r'^$', TriggerHappyHomeTemplateView.as_view(),name="th_home"),

        # ****************************************
        # auth module
        # ****************************************
        url(r'^auth/', include('django.contrib.auth.urls')),
        # ****************************************
        # customized lgout action
        # ****************************************
        url(r'^logout/$', 'django_th.views.logout_view', name='logout'),

]
