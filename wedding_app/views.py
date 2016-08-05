import datetime
import locale
import pytz

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from json import dumps as json_dumps

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Wedding, Party, Couple, Configuration
from rsvp.forms import RSVPform
from rsvp.rsvp import get_rsvp_form

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

@login_required
def home(request):
    locale.setlocale(locale.LC_ALL, 'pl_PL.utf8')

    #Get information about wedding
    wedding = Wedding.load()
    wedding.when = timezone.localtime(wedding.when)
    wedding_day = wedding.when.strftime('%A').title()
    wedding_time_json = json_dumps({'wedding_time': wedding.when}, default=date_handler)
    print(wedding.when)

    #Get information about party
    party = Party.load()
    party.when = timezone.localtime(party.when)

    #Get information about couple
    couple = Couple.load()

    #Get RSVP informations
    rsvp_form = get_rsvp_form(request.session)
    rsvp_success = request.session.get('rsvp_success', False)

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

@login_required
def party(request):
    locale.setlocale(locale.LC_ALL, 'pl_PL.utf8')

    #Get information about wedding
    wedding = Wedding.load()
    wedding.when = timezone.localtime(wedding.when)
    wedding_day = wedding.when.strftime('%A').title()

    #Get information about party
    party = Party.load()
    party.when = timezone.localtime(party.when)

    #Get information about couple
    couple = Couple.load()

    context = {
        'wedding': wedding,
        'party': party,
        'couple': couple,
        'wedding_day': wedding_day,
    }

    return render(request,
                  'wedding_app/pages/party.html',
                  context)

def user_login(request):
    username = 'user'

    if request.method == 'POST':
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('wedding:home'))
    else:
        config = Configuration.objects.all()[0]

        if config.login_required:
            form = AuthenticationForm()

            #Get information about couple
            couple = Couple.load()

            context = {
                'form': form,
                'couple': couple,
            }
            return render(request,
                   'wedding_app/pages/login.html',
                   context)
        else:
            user = User.objects.get(username=username)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if user is not None:
                login(request, user)
                return redirect(reverse('wedding:home'))

