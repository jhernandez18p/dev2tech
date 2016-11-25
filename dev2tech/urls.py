from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
# Local Apps
from local_apps.frontend import views as frontend_views
from local_apps.development import views as development_views
from local_apps.marketing import views as marketing_views
from local_apps.profiles import auth as auth_views

urlpatterns = [

    url(r'^$', frontend_views.home, name="Home" ),
    url(r'^conocenos/$', frontend_views.about_us, name="about" ),
    # Services
    url(r'^servicios/$', frontend_views.services, name="services" ),
    url(r'^servicios/full-stack/$', development_views.full_stack, name="full-stack" ),
    url(r'^servicios/story-telling/$', development_views.full_stack, name="story-telling" ),
    url(r'^servicios/marketing/$', marketing_views.marketing, name="marketing" ),
    # Done
    url(r'^proyectos/$', frontend_views.done, name="done" ),
    # Team
    url(r'^team/$', frontend_views.team, name="team" ),
    # Admin
    url(r'^adminsite/', admin.site.urls),
    # Auth
    url(r'^login/', auth_views.login, name = 'Login'),
    url(r'^logout/', auth_views.logout, name = 'Logout'),
    url(r'^register/', auth_views.login, name = 'Register'),
]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,
            {
                'document_root':settings.MEDIA_ROOT,
            }
        ),
    ]
