import datetime
from json import dumps as json_dumps

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from rsvp.forms import RSVPform
from .models import Wedding, Party, Couple

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

def home(request):
    #Get information about wedding
    wedding = Wedding.objects.all()
    wedding_day = ''
    wedding_time_json = json_dumps({'wedding_time': datetime.datetime.now()}, default=date_handler)

    if len(wedding) == 0:
        wedding = None
    else:
        wedding = wedding[0]
        wedding_day = wedding.when.strftime('%A')
        wedding_time_json = json_dumps({'wedding_time': wedding.when}, default=date_handler)

    #Get information about wedding
    party = Party.objects.all()
    if len(party) == 0:
        party = None
    else:
        party = party[0]

    #Get information about couple
    couple = Couple.objects.all()
    if len(couple) == 0:
        couple = None
    else:
        couple = couple[0]

    #Get RSVP informations
    rsvp_fields = request.session.get('rsvp_fields')
    rsvp_errors = request.session.get('rsvp_errors')
    rsvp_success = request.session.get('rsvp_success', False)

    #Add errors to RSVP form
    rsvp_form = RSVPform(rsvp_fields)
    if rsvp_errors:
        fields = rsvp_errors.keys()
        for field in fields:
            errors = rsvp_errors.get(field)
            for error in errors:
                rsvp_form.add_error(field, error)

    context = {
        'wedding': wedding,
        'party': party,
        'couple': couple,
        'wedding_day': wedding_day,
        'wedding_time_json': wedding_time_json,
        'rsvp_form': rsvp_form,
        'rsvp_success': rsvp_success,
    }

    return render(request,
                  'wedding_app/pages/home.html',
                  context)