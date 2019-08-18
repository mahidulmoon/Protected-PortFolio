from django.db import models

class Portfolio(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
