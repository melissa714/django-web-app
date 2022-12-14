from django.shortcuts import redirect, render
from  django.http import HttpResponse
from listings.models import Band,Listing
from django.shortcuts import get_object_or_404
from  .forms import ContactUsForm,BandForm,ListingForm
from django.core.mail import send_mail

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



def Contact(request):
    if request.method =='POST':
        form=ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(
                
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                message = form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['kanangemelissanguessan@gmail.com'],
            )
            return redirect('email-sent')
    else:
        form=ContactUsForm()
    return render(request,'listings/contact.html',{'form':form})



def band_detail(request,id):
    band = get_object_or_404(Band,id=id)
    return render(request,'listings/band_detail.html',{'band':band})



def email(request):
    return HttpResponse("Felicitation ok")

# listings/views.py


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form=BandForm()

    return render(request,'listings/band_create.html',{'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listings = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listings-detail', listings.id)

    else:
        form = ListingForm()

    return render(request, 'listings/listings_create.html', {'form': form})



def band_update(request,id):
    band=Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST,instance=band)
        if form.is_valid():
           form.save()
           return redirect('band-detail',band.id) 
            
    else:
        form = BandForm(instance=band)
    return render (request,'listings/band_update.html',{'form':form})



def listing_update(request,id):
    listing=Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request,"listings/listing_update.html",{'form':form})
    
    
def band_delete(request,id):
    band=Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request,'listings/band_delete.html',{'band':band})
    


def listing_delete(request,id):
    listing=Listing.objects.get(id=id) 
    if request.method == 'POST':
        listing.delete()
        return redirect('listings')
    return render(request, 'listings/band_delete.html', {'listing': listing})
