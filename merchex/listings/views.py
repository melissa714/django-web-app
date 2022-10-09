from django.shortcuts import render
from  django.http import HttpResponse
from listings.models import Band,Listing
from django.shortcuts import get_object_or_404


def about(request):
    return HttpResponse('<h1> A propos</h1> <p>Nous adorons merch!</p>')




def bands_listing(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})


def listings_detail(request,id):
    listings = Listing.objects.get(id=id)
    return render(request, 'listings/listing_details.html', {'listings': listings})



def contact(request):
    return render(request,'listings/contact.html')



def band_detail(request,id):
    band = get_object_or_404(Band,id=id)
    return render(request,'listings/band_detail.html',{'band':band})