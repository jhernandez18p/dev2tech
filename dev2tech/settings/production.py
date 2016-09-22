from dev2tech.settings.base import *


SECRET_KEY = config('DEV2TECH_SECRET_KEY')

DEBUG = config('DEV2TECH_DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = ['.dev2tech.xyz']

# AUTH_USER_MODEL = 'intra_profile.User'

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
