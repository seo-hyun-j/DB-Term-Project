from django import forms
from .models import *

class ShoesForm(forms.ModelForm):
    
    class Meta:
        model = Shoes

        fields = ('height','category_num', 'matrial_num') 




