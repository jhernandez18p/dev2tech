# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    url,
    handler400,
    handler403,
    handler404,
    handler500
)
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
# Local Apps
from settings.settings.sitemaps import StaticViewSitemap
from local_apps.profiles import auth as auth_views

handler400 = 'local_apps.frontend.views.custom_bad_request_view'
handler403 = 'local_apps.frontend.views.custom_permission_denied_view'
handler404 = 'local_apps.frontend.views.custom_page_not_found_view'
handler500 = 'local_apps.frontend.views.custom_error_view'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # frontend
    url(r'^',  include('local_apps.frontend.urls') ),
    url(r'^servicios/',  include('local_apps.services.urls') ),
    # Admin
    url(r'^adminsite/', admin.site.urls),
    # Auth
    url(r'^login/', auth_views.login, name = 'Login'),
    url(r'^logout/', auth_views.logout, name = 'Logout'),
    url(r'^register/', auth_views.login, name = 'Register'),
    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    ]
