from django import forms
from .models import *


class img_upload(forms.ModelForm):
    class Meta:
        model = image_upload
        fields = ['image']
