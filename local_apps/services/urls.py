# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
# Local Apps
from local_apps.frontend import views as frontend_views
from local_apps.services import views as services_views

urlpatterns = [
    url(r'^$', frontend_views.services, name="services" ),
    url(r'^(?P<url_name>[\w-]+)/', services_views.service_detail, name="Service_detail" ),
]
