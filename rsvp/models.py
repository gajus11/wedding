from django.db import models

class RSVP(models.Model):
    name = models.CharField(verbose_name="imię",
                            max_length=100)
    last_name = models.CharField(verbose_name="nazwisko",
                                 max_length=100)
    adults_number = models.PositiveIntegerField(verbose_name="dorośli",
                                                default=1)
    childrens_number = models.PositiveIntegerField(verbose_name="dzieci",
                                                default=0)
    transport = models.BooleanField(verbose_name="transport",
                                    default=False)
    accomodation = models.BooleanField(verbose_name="nocleg",
                                       default=False)
