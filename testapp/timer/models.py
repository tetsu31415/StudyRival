from django.db import models
from django.utils import timezone

# Create your models here.

class Record(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateField(default=timezone.now)
    time = models.IntegerField()

