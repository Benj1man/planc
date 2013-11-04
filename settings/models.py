from django.db import models

# Create your models here.
class Setting(models.Model):
    def __str__(self):
        return self.beam
    beam = models.CharField(max_length=200)
    hub = models.CharField(max_length=200)
    polarization = models.CharField(max_length=200)

class Option(models.Model):
    def __str__(self):
        return self.frequency
    setting = models.ForeignKey(Setting)
    sat_par_longitude_degrees = models.CharField(max_length=200)
    sat_par_longitude_hemisphere = models.CharField(max_length=200)
    sat_par_frequency = models.CharField(max_length=200)
    sat_par_symbol_rate = models.CharField(max_length=200)

