from django.db import models

class Slider(models.Model):
    pass

class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE)
    image = models.ImageField()
    text = models.CharField(max_length=200)

class Couple(models.Model):
    bride_name = models.CharField(verbose_name='imię_panny',
                                  max_length=100)
    bride_last_name = models.CharField(verbose_name='nazwisko_panny',
                                       max_length=100)
    groom_name = models.CharField(verbose_name='imię_kawalera',
                                  max_length=100)
    groom_last_name = models.CharField(verbose_name='nazwisko_kawalera',
                                       max_length=100)

class Wedding(models.Model):
    when = models.DateTimeField()
    where = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    #TODO:: Add google maps position

class Party(models.Model):
    when = models.DateTimeField()
    where = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=1000)
    #TODO:: Add google maps position