import datetime
from json import dumps as json_dumps

from django.shortcuts import render

from rsvp.forms import RSVPform
from .models import Wedding, Party, Couple

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

def home(request):
    #Get information about wedding and party
    wedding = Wedding.objects.all()
    wedding_day = ''
    wedding_time_json = json_dumps({'wedding_time': datetime.datetime.now()}, default=date_handler)

    if len(wedding) == 0:
        wedding = None
    else:
        wedding = wedding[0]
        wedding_day = wedding.when.strftime('%A')
        wedding_time_json = json_dumps({'wedding_time': wedding.when}, default=date_handler)

    party = Party.objects.all()
    if len(party) == 0:
        party = None
    else:
        party = party[0]

    couple = Couple.objects.all()
    if len(couple) == 0:
        couple = None
    else:
        couple = couple[0]

    #If RSVP form is submited
    rsvp_success = False

    if request.method == 'POST':
        rsvp_form = RSVPform(request.POST)
        if rsvp_form.is_valid():
            rsvp_form.save()
            rsvp_success = True

    rsvp_form = RSVPform()

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