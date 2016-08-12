from django.contrib import admin
from django import forms

from .models import Wedding, Party, Couple, Configuration

class WeddingForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Wedding
        exclude = []

class PartyForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Party
        exclude = []

class WeddingAdmin(admin.ModelAdmin):
    form = WeddingForm

class PartyAdmin(admin.ModelAdmin):
    form = PartyForm

admin.site.register(Wedding, WeddingAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Couple)
admin.site.register(Configuration)