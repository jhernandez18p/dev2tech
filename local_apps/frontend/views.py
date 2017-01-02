from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import *
import datetime
import random

from local_apps.classes import helpers
from local_apps.frontend.models import *
from local_apps.services.models import *

@login_required
def about_us(request):
    """  """
    sub_categories =SiteSubCategories.objects.all()
    for sub_category in sub_categories:
        if sub_category.sub_category == 'info':
            info_section_id = sub_category.id
        elif sub_category.sub_category == 'values':
            value_section_id = sub_category.id

    info_sections = Sections.objects.all().filter(sub_category=info_section_id)
    value_sections = list(Sections.objects.all().filter(sub_category=value_section_id))
    random.shuffle(value_sections)
    faqs = FAQ.objects.all()
    page_title = 'about'
    # print(info_sections[1])
    template =  'frontend/about.html'

    context = {
        'page_title': page_title,
        'title':'Conócenos',
        'nombre':'Josmer Hernandez',
        'info_sections': info_sections,
        'value_sections': value_sections,
        'faqs':faqs,
        'template':template,
    }

    return render(request, template, context)

@login_required
def contact(request):
    """#Contact Forms """
    if request.method == 'GET':

        return HttpResponseRedirect('/')

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        service = request.POST['service']
        sub_service = request.POST['sub_service']
        budget = request.POST['budget']
        url = request.POST['url']


        if name == '' or email == '' or comments == '':
            return HttpResponseRedirect(url)
        if service == '':
            send_mail(
                        'Email de contacto, página web',
                        '%s, ha estado visitando la página web. Su email es: %s, nos ha dejado el siguiente mensaje. \n\n\n\n\n "%s"' % (name,email,comments) ,
                        email,
                        ['contacto@dev2tech.xyz','jhernandez.18p@dev2tech.xyz'],
                        fail_silently=False,
                    )
            context = {
                'title': 'Mensaje enviado'
            }
            return HttpResponseRedirect(url)
        else:
            send_mail(
                        'Email de contacto, página web',
                        '%s, ha estado visitando la página web. Su email es: %s, nos ha dejado el siguiente mensaje. \n\n\n\n\n "%s"' % (name,email,comments) ,
                        email,
                        ['contacto@dev2tech.xyz','jhernandez.18p@dev2tech.xyz'],
                        fail_silently=False,
                    )

            context = {
                'title': 'Mensaje enviado'
            }
            return HttpResponseRedirect(url)

@login_required
def done(request):
    """  """
    technologies = Technologies.objects.all()
    page_title = 'done'
    context = {
        'page_title': page_title,
        'title':'¡Lo que hemos hecho!',
        'nombre':'Josmer Hernandez',
        'technologies':technologies,
    }

    return render(request, 'frontend/done.html',context)

@login_required
def home(request):
    """  """
    sub_categories =SiteSubCategories.objects.all()

    for sub_category in sub_categories:
        if sub_category.sub_category == 'header':
            header_subcat = sub_category
        elif sub_category.sub_category == 'all services':
            services_subcat = sub_category.id

    banners = Banners.objects.all().filter(sub_category=header_subcat)
    services = list(Services.objects.all().filter(sub_category=services_subcat))
    random.shuffle(services)
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
def services(request):
    """  """
    sub_categories =SiteSubCategories.objects.all()

    for sub_category in sub_categories:
        if sub_category.sub_category == 'all services':
            services_section_id = sub_category.id
        elif sub_category.sub_category == 'success_stories':
            value_section_id = sub_category.id

    services_section = list(Services.objects.all().filter(sub_category=services_section_id).order_by('name'))

    random.shuffle(services_section)

    page_title = 'services'
    context = {
        'page_title': page_title,
        'title':'¿Qué hacemos?',
        'nombre':'Josmer Hernandez',
        'services_section': services_section,
    }

    return render(request, 'frontend/services.html',context)

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
