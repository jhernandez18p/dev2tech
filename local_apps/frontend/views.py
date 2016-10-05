from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import datetime


@login_required
def home(request):

    context = {
        'title':'Home',
        'nombre':'Josmer Hernandez'
    }

    return render(request, 'frontend/index.html',context)
