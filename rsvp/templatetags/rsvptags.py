from django import template
from django.contrib.admin.templatetags.admin_list import result_list as admin_list_result_list, register

@register.inclusion_tag('admin/rsvp/rsvp/change_list_results_rsvp.html')
def result_list_rsvp(cl, context):
    columns = len(admin_list_result_list(cl)['result_headers'])
    rsvp_cl = {
        'total_adults': context['total_adults'],
        'total_childrens': context['total_childrens'],
        'total_transport': context['total_transport'],
        'total_accomodation': context['total_accomodation'],
        'empty_column_range': range(columns - 5),   # Empty columns in Total row
    }
    rsvp_cl.update(admin_list_result_list(cl))
    return rsvp_cl