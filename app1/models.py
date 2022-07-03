import datetime

from django.db import models

# Create your models here.

class Goods(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True, null=False)
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=500)
    time_created = models.DateTimeField(null=False, default=datetime.datetime.now)