from django.db import models

class RSVP(models.Model):
    name = models.CharField(verbose_name="imię",
                            max_length=100,
                            blank=False,
                            null=False)
    last_name = models.CharField(verbose_name="nazwisko",
                                 max_length=100,
                                 blank=False,
                                null=False)
    adults_number = models.PositiveIntegerField(verbose_name="dorośli",

                                                blank=False,
                                                null=False)
    childrens_number = models.PositiveIntegerField(verbose_name="dzieci",
                                                   blank=False,
                                                   null=False)
    transport = models.BooleanField(verbose_name="transport",
                                    default=False)
    accomodation = models.BooleanField(verbose_name="nocleg",
                                       default=False)
