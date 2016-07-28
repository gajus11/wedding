from .forms import RSVPform

def get_rsvp_form(session):
    rsvp_fields = session.get('rsvp_fields')
    rsvp_errors = session.get('rsvp_errors')
    rsvp_success = session.get('rsvp_success', False)

    #Add errors to RSVP form
    rsvp_form = RSVPform(rsvp_fields)
    if rsvp_errors:
        fields = rsvp_errors.keys()
        for field in fields:
            errors = rsvp_errors.get(field)
            for error in errors:
                rsvp_form.add_error(field, error)

    return rsvp_form