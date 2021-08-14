from django.shortcuts import render
from django.views.generic import TemplateView

class Contacts(TemplateView):
    template_name = 'footer/contacts.html'

class FAQ(TemplateView):
    template_name = 'footer/FAQ.html'

class AboutUs(TemplateView):
    template_name = 'footer/about_us.html'

class FollowUs(TemplateView):
    template_name = 'footer/follow_us.html'

class Career(TemplateView):
    template_name = 'footer/career.html'

class Sponsors(TemplateView):
    template_name = 'footer/sponsors.html'