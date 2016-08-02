from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse

from .models import RSVP
from .forms import RSVPform

def create_rsvp(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'last_name': request.POST.get('last_name'),
            'adults_number': request.POST.get('adults_number'),
            'childrens_number': request.POST.get('childrens_number'),
            'transport': request.POST.get('transport') == 'true',
            'accomodation': request.POST.get('accomodation') == 'true',
        }

        rsvp_form = RSVPform(data)

        if rsvp_form.is_valid():
            rsvp_form.save()
            request.session['rsvp_success'] = True

            return JsonResponse(
                data={},
                status=200
            )
        else:
            errors = rsvp_form.errors.as_json()

            return JsonResponse(
                {'errors': errors},
                status=400
            )