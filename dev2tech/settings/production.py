from dev2tech.settings.base import *
from decouple import config

SECRET_KEY = config('DEV2TECH_SECRET_KEY')

DEBUG = False

# ALLOWED_HOSTS = ['*.dev2tech.xyz']

AUTH_USER_MODEL = 'intra_profile.User'

STATIC_URL = 'https://%s/' % config('AWS_BUCKET_URL')

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = config('AWS_BUCKET_NAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

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
