from django import forms
from .models import Cha

class ChaForm(forms.Form):
    cha = forms.ModelChoiceField(queryset=Cha.objects.all(), label="Select Cha")
    