from django.contrib import admin

from local_apps.services.models import *

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = (
                'name',
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
                    'description',
                    'short_description',
                    'color',
                    'image',
                    'width_field',
                    'height_field',
                    'sub_category',
                )


@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    fields = (
                'name',
                'description',
                'image',
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
                    'width_field',
                    'height_field',
                    'sub_category',
                    'url',
                )
