from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Gift
from .forms import GiftForm

def gifts_list(request):
    gifts = Gift.objects.all()
    forms = []

    for gift in gifts:
        if not gift.is_reserved:
            gift.reserver = ''
        form = GiftForm(instance=gift)
        forms.append(form)

    context = {
        'gifts_forms': zip(gifts, forms),
    }

    return render(request,
                  'gifts/gifts_list.html',
                  context)

def update_gift(request, id):
    instance = get_object_or_404(Gift, id=id)
    print(instance)
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.is_reserved = True
            gift.image = instance.image
            gift.save()

    return redirect(reverse('gifts:gifts_list'))