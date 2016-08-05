from django.db import models

# class Person(models.Model):
#     name = models.CharField(verbose_name='imię',
#                             max_length=100)
#     last_name = models.CharField(verbose_name='nazwisko',
#                                  max_length=100)

class Gift(models.Model):
    name = models.CharField(verbose_name='nazwa',
                            max_length=200)
    image = models.ImageField(verbose_name='obrazek',
                              blank=True,
                              null=True)
    link = models.CharField(verbose_name='link',
                            max_length=200)
    is_reserved = models.BooleanField(verbose_name='zarezerwowane',
                                      default=False)
    reserver = models.CharField(verbose_name='osoba_rezerwująca',
                                max_length=200,
                                null=True)

    class Meta:
        verbose_name = 'prezent'
        verbose_name_plural = 'prezenty'

    def __str__(self):
        return self.name