from django.conf.urls import url
from django.contrib import admin

from local_apps.frontend import views as frontend_views

urlpatterns = [
    url(r'^$', frontend_views.home, name="Home" ),
    url(r'^admin/', admin.site.urls),
]
