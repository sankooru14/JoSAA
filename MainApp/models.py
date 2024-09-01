from django.db import models

# Create your models here.


class data(models.Model):
    institute = models.CharField(max_length=255)
    Branch = models.CharField(max_length=255)
    Category = models.CharField(max_length=255, default='OPEN')
    Gender = models.CharField(max_length=255, default='Gender-Neutral')
    Opening_rank = models.FloatField(default=1)
    Closing_rank = models.FloatField(default=99999)
    year = models.FloatField(default=2020)
    round = models.IntegerField(default=1)
