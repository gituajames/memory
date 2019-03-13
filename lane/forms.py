from django import forms
from .models import image

class imageform(forms.ModelForm):
    class Meta:
        model = image
        fields = ('description', 'image')