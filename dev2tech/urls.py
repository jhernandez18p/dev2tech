from django.conf.urls import url
from django.contrib import admin

from local_apps.frontend import views as frontend_views
from local_apps.profiles import auth as auth_views

urlpatterns = [
    url(r'^home/', frontend_views.home, name="Home" ),
    url(r'^notadminsite/', admin.site.urls),
    # Auth
    url(r'^$', auth_views.login, name = 'Login'),
    url(r'^salir/', auth_views.logout, name = 'Logout'),
    url(r'^registro/', auth_views.register, name = 'Register'),
]
