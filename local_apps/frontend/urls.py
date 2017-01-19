# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
# Local Apps
from local_apps.frontend import views as frontend_views

urlpatterns = [

    url(r'^$', frontend_views.home, name="Home" ),
    url(r'^conocenos/', frontend_views.about_us, name="about" ),
    url(r'^contacto/', frontend_views.contact, name="contact" ),
    url(r'^contratanos/', frontend_views.contract, name="contract" ),
    url(r'^proyectos/', frontend_views.done, name="done" ),
    url(r'^$', frontend_views.team, name="team" ),

    url(r'^tds/', frontend_views.home, name="loyalty" ),
    url(r'^privacidad/', frontend_views.home, name="privacy" ),

]
