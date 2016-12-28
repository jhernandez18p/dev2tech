from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
# Local Apps
from local_apps.frontend import views as frontend_views
from local_apps.profiles import auth as auth_views

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
]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    ]
