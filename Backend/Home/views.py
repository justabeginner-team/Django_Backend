from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):

    dests = Destination.objects.all()
    context_dict = {
       'dests': dests,
    }
    return render(request, 'Home/index.html', context=context_dict)


def about(request):
    return render(request, 'Home/about.html')


def destinations(request):
    return render(request, 'Home/destinations.html')


def contact(request):
    return render(request, 'Home/contact.html')


def news(request):
    return render(request, 'Home/news.html')


def elements(request):
    return render(request, 'Home/elements.html')
