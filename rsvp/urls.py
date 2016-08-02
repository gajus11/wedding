from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create_rsvp/$', views.create_rsvp, name='create_rsvp'),
]