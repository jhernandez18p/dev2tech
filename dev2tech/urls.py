from django.conf.urls import url
from django.contrib import admin

# Local Apps
from local_apps.frontend import views as frontend_views
from local_apps.profiles import auth as auth_views

urlpatterns = [

    url(r'^$', frontend_views.home, name="Home" ),
    url(r'^notadminsite/', admin.site.urls),

    # Auth
    url(r'^login/', auth_views.login, name = 'Login'),
    url(r'^logout/', auth_views.logout, name = 'Logout'),
    url(r'^register/', auth_views.register, name = 'Register'),

]
