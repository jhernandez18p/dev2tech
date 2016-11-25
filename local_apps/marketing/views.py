from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import datetime


def marketing(request):
    """  """
    page_title = 'services'
    context = {
        'page_title': page_title,
        'title':'Somos Marketing',
        'nombre':'Josmer Hernandez'
    }

    return render(request, 'marketing/marketing.html',context)
