from django.db import models

class Report(models.Model):
    username = models.CharField(max_length=25, default='', blank=True)
    address = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
