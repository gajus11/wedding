from django import forms
from .models import RSVP

class RSVPform(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'
        localized_fields = '__all__'
        widgets = {
            'adults_number': forms.NumberInput(attrs={
                'min': '1', 'max': '10', 'step': '1', 'placeholder': '> 18 lat', 'class': 'form-control',
            }),
            'childrens_number': forms.NumberInput(attrs={
                'min': '0', 'max': '10', 'step': '1', 'placeholder': '< 18 lat', 'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={'placeholder': 'Imię', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko', 'class': 'form-control'}),
            'transport': forms.CheckboxInput(),
            'accomodation': forms.CheckboxInput(),
        }