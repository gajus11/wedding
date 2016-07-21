from django.contrib import admin
from .models import Gift

class GiftAdmin(admin.ModelAdmin):
    list_display = ['name' ,'image', 'link',
                    'is_reserved', 'reserver']

# Register your models here.
admin.site.register(Gift, GiftAdmin)