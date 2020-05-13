from django.urls import path
from . import views  # from all

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destination'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('elements', views.elements, name='elements')
]
