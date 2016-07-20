from django.shortcuts import render

from rsvp.forms import RSVPform

def home(request):
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