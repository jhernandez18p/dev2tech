from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from local_apps.services.models import *

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = (
                'name',
                'title',
                'url_name',
                'description',
                'short_description',
                'color',
                'image',
                'width_field',
                'height_field',
                'sub_category',
            )
    search_fields = ['name',]
    list_display = (
                    'name',
                    'title',
                    'url_name',
                    'description',
                    'short_description',
                    'color',
                    'image',
                    'width_field',
                    'height_field',
                    'sub_category',
                )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = (
                'title',
                'sub_title',
                'description',
                'position',
                'color',
                'image',
                'width_field',
                'height_field',
                'services',
            )
    search_fields = ['title','sub_title',]
    list_display = (
                    'title',
                    'sub_title',
                    'description',
                    'color',
                    'image',
                    'width_field',
                    'height_field',
                    'services',
                )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    fields = (
                'name',
                'description',
                'image',
                'color',
                'width_field',
                'height_field',
                'sub_category',
                'url',
            )
    search_fields = ['name',]
    list_display = (
                    'name',
                    'description',
                    'image',
                    'color',
                    'width_field',
                    'height_field',
                    'sub_category',
                    'url',
                )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

@admin.register(Promos)
class PromosAdmin(admin.ModelAdmin):
    fields = (
                'title',
                'sub_title',
                'description',
                'color',
                'image',
                'width_field',
                'height_field',
                'services',
            )
    search_fields = ['title',]
    list_display = (
                    'title',
                    'sub_title',
                    'description',
                    'color',
                    'image',
                    'width_field',
                    'height_field',
                    'services',
                )

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
