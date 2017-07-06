# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class CastMember(models.Model):
    '''
    For now, this model allows for the current character bio to be included.

    In the future as characters die or campaigns progress, we may want to create
    a Character model and tie the current character to this model.

    This would also allow for a cross reference to characters in past campaigns
    and would create a "Past Characters" section in the cast's page. We could
    then create a character page for each one which the variable "Campaign"

    '''
    FirstName = models.CharField(max_length=100)

    LastName = models.CharField(max_length=100)

    Photo = models.ImageField(upload_to = 'cast_images',
                              default = 'cast_images/loser.jpg')

    Bio = models.TextField()

    Silhouette = models.ImageField(upload_to = 'cast_images',
                                   default = 'cast_images/imabear.png')

    CharacterName = models.TextField(max_length=100)

    CharacterBio = models.TextField()

    def FullName(self):
        return (self.FirstName + ' ' + self.LastName)

    '''Twitter =

    Facebook =

    OtherSite = '''

    slug = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.s = slugify(self.slug)
        super(CastMember, self).save(*args, **kwargs)


    def __str__(self):
        return self.FullName()

'''class Character(models.Model):
    Player = models.ForeignKey(CastMember, default=1, null=True)

    CharacterName = models.TextField(max_length=100)

    CharacterBio = models.TextField()

    CharacterPic = models.ImageField(upload_to = 'cast/static/char_images',
                                     default = 'cast/static/char_images/lame.jpg')

    '''
