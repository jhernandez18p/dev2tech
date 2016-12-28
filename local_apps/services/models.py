# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from local_apps.frontend.models import SiteSubCategories
from local_apps.frontend.models import Colors as Frontend_Colors

class Services(models.Model):
    """# Class for services """
    name = models.CharField(max_length=144)
    title = models.CharField(max_length=144, blank=True)
    url_name = models.CharField(max_length=60)
    description = models.TextField()
    short_description = models.TextField(blank=True,)
    color = models.ForeignKey(
                                    Frontend_Colors,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                )
    image = models.ImageField(
                                upload_to='services',
                                width_field="width_field",
                                height_field="height_field",
                                blank=True,
                            )
    width_field = models.IntegerField(default=0, blank=True,)
    height_field = models.IntegerField(default=0, blank=True,)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE,
                                )

    def get_absolute_url(self):
        """ Url path """
        return '/servicios/%s/' % self.url_name

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Dev2tech Services')
        verbose_name_plural = ('Dev2tech Services')


class Service(models.Model):
    """# Class for the services of a global service """
    title = models.CharField(max_length=144)
    sub_title = models.CharField(max_length=144, blank=True)
    description = models.TextField()
    color = models.ForeignKey(
                                    Frontend_Colors,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                )
    image = models.ImageField(
                                upload_to='services/service/',
                                width_field="width_field",
                                height_field="height_field",
                                blank=True,
                            )
    width_field = models.IntegerField(default=0, blank=True,)
    height_field = models.IntegerField(default=0, blank=True,)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    services = models.ForeignKey(
                                    Services,
                                    on_delete=models.CASCADE,
                                )

    def __str__(self):
        return self.title

    class Meta:
        """# Class Meta"""
        verbose_name = ('Dev2tech Services | Service')
        verbose_name_plural = ('Dev2tech Services | Service')


class Technologies(models.Model):
    """# Class for the Technologies we use"""
    name = models.CharField(max_length=144)
    description = models.TextField()
    image = models.ImageField(
                                upload_to='technologies',
                                width_field="width_field",
                                height_field="height_field",
                                blank=True,
                            )
    width_field = models.IntegerField(default=0, blank=True,)
    height_field = models.IntegerField(default=0, blank=True,)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    color = models.ForeignKey(
                                Frontend_Colors,
                                on_delete=models.CASCADE,
                                blank=True,
                            )
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE,
                                )
    url = models.CharField(max_length=144, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        """# Class Meta"""
        verbose_name = ('Technologie')
        verbose_name_plural = ('Technologies')


class Promos(models.Model):
    """# Class for the promo of the service of services"""
    title = models.CharField(max_length=144)
    sub_title = models.CharField(max_length=144, blank=True)
    description = models.TextField()
    color = models.ForeignKey(
                                    Frontend_Colors,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                )
    image = models.ImageField(
                                upload_to='services/Promos/',
                                width_field="width_field",
                                height_field="height_field",
                                blank=True,
                            )
    width_field = models.IntegerField(default=0, blank=True,)
    height_field = models.IntegerField(default=0, blank=True,)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    services = models.ForeignKey(
                                    Services,
                                    on_delete=models.CASCADE,
                                )
    def __str__(self):
        return self.title

    class Meta:
        """# Class Meta"""
        verbose_name = ('Promo')
        verbose_name_plural = ('Promos')
