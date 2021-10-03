from django.urls import path
from .views import AboutusPageView, DonationsPageView, FeedbackPageView, HelpPageView, HomePageView ,ContactPageView, OffersnowPageView, PackagesPageView, PrivacypolicyPageView, HelpPageView 


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('aboutus', AboutusPageView.as_view(), name ='aboutus'),
    path('privacypolicy', PrivacypolicyPageView.as_view(), name='privacypolicy'),
    path('help' , HelpPageView.as_view(), name='help'),
    path('offersnow' , OffersnowPageView.as_view(), name='offersnow'),
    path('packages', PackagesPageView.as_view(), name='packages'),
    path('donations', DonationsPageView.as_view(), name='donations'),
    path('feedback', FeedbackPageView.as_view(), name='feedback'),



]