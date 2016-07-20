from django.db import models

class Person(models.Model):
    name = models.CharField(verbose_name='imię',
                            max_length=100)
    last_name = models.CharField(verbose_name='nazwisko',
                                 max_length=100)

class Gift(models.Model):
    name = models.CharField(verbose_name='nazwa',
                            max_length=200)
    image = models.ImageField(verbose_name='obrazek')
    link = models.CharField(verbose_name='link',
                            max_length=200)
    is_reserved = models.BooleanField(verbose_name='zarezerwowane',
                                      default=False)
    reserver = models.ForeignKey(Person,
                                 verbose_name='osoba_rezerwująca')