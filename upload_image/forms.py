# forms.py
from django import forms
from .models import *


class upload(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['image']
