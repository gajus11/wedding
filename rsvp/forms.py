from django.forms import ModelForm
from .models import RSVP

class RSVPform(ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'
        localized_fields = '__all__'
        # fields = ['name', 'last_name', 'adults_number',
        #           'children_number', 'transport', 'accomodation']