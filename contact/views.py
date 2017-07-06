# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            email = form.cleaned_data['email']
            Message = form.cleaned_data['Message']
            try:
                send_mail(Name, Message, email, ['expandgold@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')
            messages.success(request, 'Success! Thank you for your message!')

    return render(request, 'contact.html', {'form': form, })
