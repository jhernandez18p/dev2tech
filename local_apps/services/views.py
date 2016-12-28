from django.shortcuts import render
import random
from .models import *

# Create your views here.
def service_detail(request,url_name=None):
    """# Sub Services Detail view"""
    service = Services.objects.get(url_name=url_name)
    services = list(Service.objects.all().filter(services = service.id))
    random.shuffle(services)
    template = 'services/detail.html'
    page_title = 'services'
    context = {
        'page_title': page_title,
        'title':str(service.name),
        'service':service,
        'sub_service': services,
    }
    return render(request, template, context)
