from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import RSVP
from .forms import RSVPform

def accept(request):
    if request.method == 'POST':
        rsvp_form = RSVPform(request.POST)
        if rsvp_form.is_valid():
            rsvp_form.save()
            request.session['rsvp_success'] = True
        #Add fields to session
        request.session['rsvp_fields'] = rsvp_form.cleaned_data
        #Add errors to session
        request.session['rsvp_errors'] = rsvp_form.errors
    address = reverse('wedding:home')
    return redirect(address + '#rsvp')