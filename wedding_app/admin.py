from django.contrib import admin

from .models import Wedding, Party, Couple, Configuration

admin.site.register(Wedding)
admin.site.register(Party)
admin.site.register(Couple)
admin.site.register(Configuration)