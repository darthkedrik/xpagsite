# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .models import Episode

# One view with a showcase for the most recent episode, then each of the 20 previous ones listed below
# paginate the second part to allow for it to go back or fore

class EpisodeListing(generic.TemplateView):
    def get(self, request, **kwargs):

        episode_list = Episode.objects.order_by('-Date')
        paginator = Paginator(episode_list[1:], 20) #Ignore most recent

        page = request.GET.get('page')

        try:
            episodes = paginator.page(page)
        except PageNotAnInteger:
            episodes = paginator.page(1)
        except EmptyPage:
            episodes = paginator.page(paginator.num_pages)

        index = episodes.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 3 if index <= max_index -3 else max_index

        page_range = list(paginator.page_range)[start_index:end_index]

        return render(request, 'episodes.html', {'episodes': episodes,
                                                 'recent': episode_list[0],
                                                 'page_range': page_range})
