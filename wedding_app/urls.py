from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^party/$', views.party, name='party'),
]