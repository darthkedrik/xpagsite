# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html')
