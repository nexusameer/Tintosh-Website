from django.urls import path
from .views import *

urlpatterns =[
    path('', IndexPage.as_view(), name='index'),
    path('portfolio/', PortfolioView.as_view(),name='portfolio'),
    path('portfolio/filter/', FilterPortfolioView.as_view(),name='filter-portfolio'),
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/',Service.as_view(), name='service'),
    
]