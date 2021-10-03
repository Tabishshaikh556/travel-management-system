from django.urls import path
from .views import HelpPageView, HomePageView ,ContactPageView, HelpPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('help', HelpPageView.as_view(), name='help'),
]