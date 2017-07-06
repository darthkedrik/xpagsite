# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#class Episode(models.Model):

    # Each episode should have a title, synopsis, soundcloud link, episode number, and upload date
class Episode(models.Model):
    Title = models.CharField(max_length=150)
    Synopsis = models.TextField()
    Date = models.DateTimeField('Published On')
    Number = models.SmallIntegerField(unique=True)

    SoundCloud = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.Title
