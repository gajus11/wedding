from datetime import datetime

from django.db import models
from django import forms

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Slider(models.Model):
    pass

class SliderImage(SingletonModel):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE)
    image = models.ImageField()
    text = models.CharField(max_length=200)

class Couple(SingletonModel):
    bride_name = models.CharField(verbose_name='imię_panny',
                                  max_length=100,
                                  default='Bride')
    bride_last_name = models.CharField(verbose_name='nazwisko_panny',
                                       max_length=100,
                                       default='Smith')
    groom_name = models.CharField(verbose_name='imię_kawalera',
                                  max_length=100,
                                  default='Groom')
    groom_last_name = models.CharField(verbose_name='nazwisko_kawalera',
                                       max_length=100,
                                       default='Smith')

    class Meta:
        verbose_name = 'para młoda'
        verbose_name_plural = 'para młoda'

    def __str__(self):
        return 'Para młoda'

class Wedding(SingletonModel):
    when = models.DateTimeField(verbose_name='kiedy',
                                default=datetime.now())
    where = models.CharField(verbose_name='kościół',
                             max_length=200,
                             default='Wedding place')
    image = models.ImageField(verbose_name='obrazek',
                              blank=True)
    description = models.CharField(verbose_name='opis',
                                   max_length=1000,
                                   default='Wedding description')
    address = models.CharField(verbose_name='adres',
                               max_length=200,
                               default='plac Defilad, Warszawa')

    class Meta:
        verbose_name = 'ślub'
        verbose_name_plural = 'ślub'

    def __str__(self):
        return 'Ślub'

class Party(SingletonModel):
    when = models.DateTimeField(verbose_name='kiedy',
                                default=datetime.now())
    where = models.CharField(verbose_name='sala',
                             max_length=200,
                             default='Party place')
    image = models.ImageField(verbose_name='obrazek',
                              blank=True)
    description = models.CharField(verbose_name='opis',
                                   max_length=1000,
                                   default='Party description')
    address = models.CharField(verbose_name='adres',
                               max_length=200,
                               default='plac Defilad, Warszawa')

    class Meta:
        verbose_name = 'wesele'
        verbose_name_plural = 'wesele'

    def __str__(self):
        return 'Wesele'

class Configuration(SingletonModel):
    login_required = models.BooleanField(verbose_name='logowanie',
                                         default=True)

    class Meta:
        verbose_name = "konfiguracja"
        verbose_name_plural = "konfiguracja"

    def __str__(self):
        return 'Konfiguracja'