from django.conf.urls import url, include
from django.contrib import admin

 
urlpatterns = [
    url(r'^',  include('front.urls')),
    url(r'^notanadminsite/', admin.site.urls),
]
