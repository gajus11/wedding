from django.shortcuts import render

from rsvp.forms import RSVPform

def home(request):
    form = RSVPform()

    context = {
        'form': form,
    }

    return render(request,
                  'wedding_app/pages/home.html',
                  context)