from settings.settings.base import *

STATICFILES_DIRS = ('',)

STATIC_ROOT = os.path.abspath(os.path.join(os.path.join(BASE_DIR,os.pardir),'staticfiles'))

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
