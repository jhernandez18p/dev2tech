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

def about_us(request):
    """  """
    sub_categories = SiteSubCategories.objects.all()
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
    template = 'frontend/about.html'

    context = {
        #'page_title': page_title,
        'pg_title':'Conócenos',
        'nombre':'Josmer Hernandez',
        'info_sections': info_sections,
        'value_sections': value_sections,
        'faqs':faqs,
        'template':template,
        'url':'/conocenos/',
    }

    return render(request, template, context)

def contract(request):
    """#Contact Forms """
    if request.method == 'GET':

        return HttpResponseRedirect('/')

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        comments = request.POST['comments']
        url = request.POST['url']

        if name == '':
            return HttpResponseRedirect(url)
        elif email == '':
            return HttpResponseRedirect(url)
        elif comments == '':
            return HttpResponseRedirect(url)

        send_mail(
            'Email de contacto, página web',
            '''
            %s, ha estado visitando la página web.
            Su email es: %s, nu númer telefónico es: %s
            nos ha dejado el siguiente mensaje. \n
             "%s"
             ''' % (name, email, number, comments),
            email,
            ['contacto@dev2tech.xyz', 'jhernandez.18p@dev2tech.xyz'],
            fail_silently=False,
        )

        context = {
            'pg_title': 'Mensaje enviado'
        }
        return HttpResponseRedirect("/")

def contact(request):
    """#Contact Forms """
    if request.method == 'GET':

        return HttpResponseRedirect('/')

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        url = request.POST['url']
        service = request.POST['service']
        if request.POST['sub_service']:
            sub_service = request.POST['sub_service']
        else:
            sub_service = "unknown"
        budget = request.POST['budget']

        if name == ''or email == '' or comments == '' or service == '' or sub_service == '' or budget == '':
            return HttpResponseRedirect(url)

        send_mail(
		            'Email de contacto, página web',
		            '%s, ha estado visitando la página web. Su email es: %s, nos ha dejado el siguiente mensaje. \n "%s" "%s" "%s" "%s"' % (name,email,comments,service,sub_service,budget) ,
		            email,
		            ['contacto@dev2tech.xyz','jhernandez.18p@dev2tech.xyz'],
		            fail_silently=False,
		        )

        context = {
            'pg_title': 'Mensaje enviado'
        }
        return HttpResponseRedirect(url)

def done(request):
    """  """
    technologies = Technologies.objects.all()
    page_title = 'done'
    context = {
        #'page_title': page_title,
        'pg_title':'¡Lo que hemos hecho!',
        'nombre':'Josmer Hernandez',
        'technologies':technologies,
        'url':'/proyectos/',
    }

    return render(request, 'frontend/done.html',context)

def home(request):
    """  """
    template = 'frontend/index.html'
    context = {
        'pg_title':'Inicio',
        'url':'/',
    }
    # sub_categories =SiteSubCategories.objects.all()

    # for sub_category in sub_categories:
    #     if sub_category.sub_category == 'header':
    #         header_subcat = sub_category
    #     elif sub_category.sub_category == 'all services':
    #         services_subcat = sub_category.id

    # banners = Banners.objects.all().filter(sub_category=header_subcat)
    # services = list(Services.objects.all().filter(sub_category=services_subcat))
    # random.shuffle(services)


    return render(request, template, context)


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
        #'page_title': page_title,
        'pg_title':'¿Qué hacemos?',
        'nombre':'Josmer Hernandez',
        'services_section': services_section,
        'url':'/servicios/',
    }

    return render(request, 'frontend/services.html',context)


def team(request):
    """  """
    page_title = 'team'
    context = {
        'news':False,
        #'page_title': page_title,
        'pg_title':'El equipo',
        'nombre':'Josmer Hernandez',
        'url':'/team/',
    }

    return render(request, 'frontend/team.html', context)


# def development(request):
#     """# Web development service """

#     template = 'services/development.html'
#     context = {
#         'title': 'development',
#         'quotation_color':'red',
#     }
#     return render(request,template,context)

# def email(request):
#     """# Email service"""

#     template = 'services/email.html'
#     context = {
#         'title': 'email',
#         'quotation_color':'red',
#     }
#     return render(request,template,context)

# def infra(request):
#     """# Infraestructure service"""

#     template = 'services/infra.html'
#     context = {
#         'title': 'infra',
#         'quotation_color':'red',
#     }
#     return render(request,template,context)

# def marketing(request):
#     """# Marketing service"""

#     template = 'services/marketing.html'
#     context = {
#         'title': 'marketing',
#         'quotation_color':'red',
#     }
#     return render(request,template,context)

# def storytelling(request):
#     """# Storytelling service"""

#     template = 'services/storytelling.html'
#     context = {
#         'title': 'storytelling',
#         'quotation_color':'red',
#     }
#     return render(request,template,context)
