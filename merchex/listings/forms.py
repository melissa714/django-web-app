from django import forms 
from listings.models import Band

class ContactUsForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField(max_length=100)
    
    
    
class BandForm(forms.ModelForm):
    class Meta:
        model =Band
        fields = '__all__'