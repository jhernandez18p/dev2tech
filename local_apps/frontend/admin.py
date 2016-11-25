# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

@admin.register(SiteCategories)
class SiteCategoriesAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to banners """

    fields = ('category',)
    search_fields = ['category',]
    list_display = ('category',)

@admin.register(SiteSubCategories)
class SiteSubCategoriesAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to banners """

    fields = ('sub_category','category',)
    search_fields = ['sub_category','category',]
    list_display = ('sub_category','category',)

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to banners """

    fields = ('name','background_color','sub_category','image','width_field','height_field',)
    search_fields = ['name','background_color','sub_category']
    list_display = ('name','background_color','sub_category','image','width_field','height_field',)


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to site info """

    fields = ('name','sub_category','description',)
    search_fields = ['name','sub_category']
    list_display = ('name','sub_category','description',)


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to site info """

    fields = (
                'title',
                'content',
                'description',
                'css_classes',
                'sub_category',
                'link',
                'image',
                'width_field',
                'height_field',
            )
    list_display = (
                    'title',
                    'content',
                    'description',
                    'css_classes',
                    'sub_category',
                    'link',
                    'image',
                    'width_field',
                    'height_field',
                )
    search_fields = ['name','sub_category']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """ Panel Admin, fields to site info """

    fields = ('question','sub_category','answers','created',)
    search_fields = ['question','sub_category']
    list_display = ('question','sub_category','answers','created',)
