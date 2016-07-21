from django.shortcuts import render

from django.conf import settings
from django.templatetags.static import static

from rsvp.forms import RSVPform

def home(request):
    print(settings.STATIC_ROOT)
    print(static('vendor/bootstrap/css/bootstrap.min.css'))
    #If form is submited
    success = False

    if request.method == 'POST':
        form = RSVPform(request.POST)
        if form.is_valid():
            form.save()
            success = True

    form = RSVPform()

    context = {
        'form': form,
        'success': success,
    }

    return render(request,
                  'wedding_app/pages/home.html',
                  context)