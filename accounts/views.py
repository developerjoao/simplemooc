# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    template_name = 'accounts/register.html'
    context = {
        'form' : UserCreationForm()
    }
    return render(request, template_name,context)


# Create your views here.