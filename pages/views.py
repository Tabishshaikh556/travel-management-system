from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class AboutusPageView(TemplateView):
    template_name = 'aboutus.html'
    
class PrivacypolicyPageView(TemplateView):
    template_name = 'privacypolicy.html'

class HelpPageView(TemplateView):
    template_name = 'help.html'

class OffersnowPageView(TemplateView):
    template_name = 'offersnow.html'

class PackagesPageView(TemplateView):
    template_name = 'packages.html'

class DonationsPageView(TemplateView):
    template_name = 'donations.html'

class FeedbackPageView(TemplateView):
    template_name = 'feedback.html'
                
