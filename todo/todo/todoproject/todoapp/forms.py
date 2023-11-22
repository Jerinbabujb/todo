from .models import too
from django import forms

class fo(forms.ModelForm):
    class Meta:
        model=too
        fields=['name','priority','date']

