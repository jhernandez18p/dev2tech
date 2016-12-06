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
    url(r'^conocenos/$', frontend_views.about_us, name="about" ),
    url(r'^contacto/$', frontend_views.contact, name="contact" ),
    url(r'^servicios/$', frontend_views.services, name="services" ),
    url(r'^servicios/full-stack$', frontend_views.development, name="dev" ),
    url(r'^servicios/correos$', frontend_views.email, name="email" ),
    url(r'^servicios/infra$', frontend_views.infra, name="infra" ),
    url(r'^servicios/marketing$', frontend_views.marketing, name="marketing" ),
    url(r'^servicios/storytelling$', frontend_views.storytelling, name="storytelling" ),
    url(r'^proyectos/$', frontend_views.done, name="done" ),
    url(r'^team/$', frontend_views.team, name="team" ),

    url(r'^tds/$', frontend_views.home, name="loyalty" ),
    url(r'^privacidad/$', frontend_views.home, name="privacy" ),

]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    ]
