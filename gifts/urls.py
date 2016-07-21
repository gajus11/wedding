from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.gifts_list, name='gifts_list'),
    url(r'^(?P<id>[0-9]+)/$', views.update_gift, name='update_gift'),
]