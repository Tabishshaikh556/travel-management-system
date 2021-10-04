from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from pages.models import BookNow,  CustomerProfile


class HomePageView(ListView):
    context_object_name = 'destination'
    model = BookNow
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

class ProfileView(CreateView):
    model = CustomerProfile
    template_name = 'customer/customerdetails.html'
    fields = ['full_name','age','gender','contact_no','email_add','address', 'place_you_want_to_visit']

class ThankyouPageView(TemplateView):
    template_name = 'thankyou.html'

        
                
