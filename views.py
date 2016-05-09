# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class TriggerHappyHomeTestTemplateView(TemplateView):
    template_name = "main.html"


class TriggerHappyHomeTemplateView(TemplateView):
    template_name = "th_home.html"

class TriggerHappyInfosTemplateView(TemplateView):
    template_name = "infos.html"


class TriggerHappyDevsTemplateView(TemplateView):
    template_name = "devs.html"


class TriggerHappyContactTemplateView(TemplateView):
    template_name = "contact.html"

