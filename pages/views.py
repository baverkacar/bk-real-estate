from django.shortcuts import render
from django.http import HttpResponse 
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    # Selecting latest 3 listing in listings database.
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()
    context = {
        'realtors' : realtors
    }
    return render(request, 'pages/about.html', context)