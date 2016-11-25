from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import *
import datetime

from local_apps.frontend.models import *

@login_required
def home(request):
    """  """

    category = SiteCategories.objects.get(category='Home')
    sub_categories =SiteSubCategories.objects.all()

    for sub_category in sub_categories:
        if sub_category.sub_category == 'header':
            header_subcat = sub_category
        if sub_category.sub_category == 'services':
            services_subcat = sub_category

    banners = Banners.objects.all().filter(sub_category=header_subcat)
    services = Sections.objects.all().filter(sub_category=services_subcat)
    page_title = 'Home'

    context = {
        'page_title': page_title,
        'title':'Home',
        'banners':banners,
        'nombre':'Josmer Hernandez',
        'services':services,
    }

    return render(request, 'frontend/index.html',context)

@login_required
def about_us(request):
    """  """

    category = SiteCategories.objects.get(category='About-us')
    sub_categories =SiteSubCategories.objects.all().filter(category=category.id)

    for sub_category in sub_categories:
        if sub_category.sub_category == 'info':
            info_section_id = sub_category.id
        elif sub_category.sub_category == 'values':
            value_section_id = sub_category.id

    info_sections = Sections.objects.all().filter(sub_category=info_section_id)
    value_sections = Sections.objects.all().filter(sub_category=value_section_id)
    faqs = FAQ.objects.all()
    page_title = 'about'
    # print(info_sections[1])

    context = {
        'page_title': page_title,
        'title':'Conócenos',
        'nombre':'Josmer Hernandez',
        'info_sections': info_sections,
        'value_sections': value_sections,
        'faqs':faqs,
    }

    return render(request, 'frontend/about.html',context)

@login_required
def services(request):
    """  """
    category = SiteCategories.objects.get(category='Services')
    sub_categories =SiteSubCategories.objects.all().filter(category=category.id)

    for sub_category in sub_categories:
        if sub_category.sub_category == 'all services':
            services_section_id = sub_category.id
        elif sub_category.sub_category == 'success_stories':
            value_section_id = sub_category.id

    services_section = Sections.objects.all().filter(sub_category=services_section_id).order_by('title')

    page_title = 'services'
    context = {
        'page_title': page_title,
        'title':'¿Qué hacemos?',
        'nombre':'Josmer Hernandez',
        'services_section': services_section,
    }

    return render(request, 'frontend/services.html',context)

@login_required
def done(request):
    """  """
    page_title = 'done'
    context = {
        'page_title': page_title,
        'title':'¡Lo que hemos hecho!',
        'nombre':'Josmer Hernandez'
    }

    return render(request, 'frontend/done.html',context)

@login_required
def team(request):
    """  """
    page_title = 'team'
    context = {
        'page_title': page_title,
        'title':'Dev2team',
        'nombre':'Josmer Hernandez'
    }

    return render(request, 'frontend/team.html',context)
