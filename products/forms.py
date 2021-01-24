from django import forms 
from .models import Product 
from Shop.models import Store



class ProdForm(forms.Form):
    class Meta:
        model = Product
        fields = ('title', 'img','price','category','store','desceiption','quantity' )