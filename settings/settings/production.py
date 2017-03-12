from settings.settings.base import *
from decouple import config

DEBUG = config('DEBUG')

WSGI_APPLICATION = 'settings.wsgi_prod.application'

ALLOWED_HOSTS = ['www.dev2tech.xyz','www.dev2tech.xyz']

DATABASES ={
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('DEV2TECH_DB_NAME'),
                'USER': config('DEV2TECH_DB_USER'),
                'PASSWORD': config('DEV2TECH_DB_PASSWORD'),
                'HOST': config('DEV2TECH_DB_HOST'),
                'PORT': config('DEV2TECH_DB_PORT',cast=int),
                }
            }
