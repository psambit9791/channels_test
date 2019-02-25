from django.db import models
from django.utils import timezone

# Create your models here.

class AccData(models.Model):
    x = models.DecimalField(max_digits=25, decimal_places=22)
    y = models.DecimalField(max_digits=25, decimal_places=22)
    z = models.DecimalField(max_digits=25, decimal_places=22)
    t = models.DecimalField(max_digits=13, decimal_places=3)