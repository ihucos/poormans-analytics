from django.db import models


class Views(models.Model):
    date = models.DateField()
    counter = models.PositiveIntegerField(default=0)

