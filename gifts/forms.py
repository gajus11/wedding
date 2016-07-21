from django import forms
from .models import Gift

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        exclude = ['image']
        widgets = {
            'name': forms.HiddenInput(),
            'link': forms.HiddenInput(),
            'is_reserved': forms.HiddenInput(),
        }