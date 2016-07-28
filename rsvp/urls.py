from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'accept/$', views.accept, name='accept'),
]