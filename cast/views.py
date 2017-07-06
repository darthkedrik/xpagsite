# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import CastMember

class CastHome(generic.ListView):

    ''' This is a simple pass to the html file.

    In the future, after campaigns have concluded, we will likely
    want to create a campaign model and have links to past campaigns
    which specific episodes and details about the story.

    '''

    model = CastMember
    template_name = 'cast.html'

    def get(self, request, **kwargs):
        allCast = CastMember.objects.all()
        return render(request, 'cast.html',
                      context={'castmembers': allCast})

class CastMemberPage(generic.DetailView):

    model = CastMember
    template_name = 'member.html'

    def fullname(self):
        return FullName()
