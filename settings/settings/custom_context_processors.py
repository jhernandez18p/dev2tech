# -*- coding: utf-8 -*-
import random
# from local_apps.services.models import Services

def menu(request):
    # top_services = list(Services.objects.all())
    # random.shuffle(top_services)
    context = {
        'menu_es':["inicio","conocenos","¿qué hacemos?","¡lo hemos hecho!","contacto",],
        'menu_en':["home","who we are","what we do?","what we´ve done?","contact",],
        # 'Top_5_Services':top_services,
    }
    return context
