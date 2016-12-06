# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from local_apps.frontend.models import SiteSubCategories

class Services(models.Model):
    """# Class for services """
    name = models.CharField(max_length=144)
    description = models.TextField()
    short_description = models.TextField()
    color = models.CharField(max_length=7)
    image = models.ImageField(
                                upload_to='services',
                                width_field="width_field",
                                height_field="height_field"
                            )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE
                                )

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Service')
        verbose_name_plural = ('Services')


class Technologies(models.Model):
    """# Class for the Technologies we use"""
    name = models.CharField(max_length=144)
    description = models.TextField()
    image = models.ImageField(
                                upload_to='technologies',
                                width_field="width_field",
                                height_field="height_field"
                            )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE
                                )
    url = models.CharField(max_length=144)

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Technologie')
        verbose_name_plural = ('Technologies')
