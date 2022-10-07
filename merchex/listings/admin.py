from django.contrib import admin

# Register your models here.
from listings.models import Band,Listing


class BandAdmin(admin.ModelAdmin): 
    list_display =('name','year_formed','genre')

admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('Title', 'band')  # ajouter ‘band' ici
admin.site.register(Listing,ListingAdmin)