from django.contrib import admin
from django.db.models import Sum
from .models import RSVP

class RSVPAdmin(admin.ModelAdmin):
    change_list_template = 'admin/rsvp/rsvp/change_list_rsvp.html'

    def get_total_adults(self):
        total = RSVP.objects.all().aggregate(total_adults=Sum('adults_number'))['total_adults']
        return total

    def get_total_childrens(self):
        total = RSVP.objects.all().aggregate(total_childrens=Sum('childrens_number'))['total_childrens']
        return total

    def get_total_transport(self):
        """
        Get total number of people (adults + children) who needed transport.
        :return:
        """
        people_list = RSVP.objects.filter(transport=True)
        if len(people_list) is 0:
            return 0
        total = people_list.aggregate(total=Sum('adults_number')+Sum('childrens_number'))['total']
        return total

    def get_total_accomodation(self):
        """
        Get total number of people (adults + children) who needed accomodation.
        :return:
        """
        people_list = RSVP.objects.filter(accomodation=True)
        if len(people_list) is 0:
            return 0
        total = people_list.aggregate(total=Sum('adults_number')+Sum('childrens_number'))['total']
        return total

    def changelist_view(self, request, extra_context=None):
        # Context send to result_list_rsvp in rsvptags.py
        context = {
            'totals': {
                'total_adults': self.get_total_adults(),
                'total_childrens': self.get_total_childrens(),
                'total_transport': self.get_total_transport(),
                'total_accomodation': self.get_total_accomodation(),
            },
        }

        return super(RSVPAdmin, self).changelist_view(request,
                                                      extra_context=context)

    list_display = ['name', 'last_name', 'adults_number',
                    'childrens_number', 'transport', 'accomodation']

admin.site.register(RSVP, RSVPAdmin)
# admin.site.register(RSVP)
