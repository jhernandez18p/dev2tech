# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class SiteCategories(models.Model):
    """ Here we define the site categories """

    category = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:

        verbose_name = ('Site category')
        verbose_name_plural = ('Site categories')
        ordering = ['-category',]


class SiteSubCategories(models.Model):
    """ Here we define the site categories """


    sub_category = models.CharField(max_length=70)
    category = models.ForeignKey(
                                    SiteCategories,
                                    on_delete=models.CASCADE
                                )
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.sub_category

    class Meta:

        verbose_name = ('Site sub-category')
        verbose_name_plural = ('Site sub-categories')
        ordering = ['-sub_category',]


class Banners(models.Model):
    """ Model media """

    name = models.CharField(max_length=70)
    background_color = models.CharField(max_length=70)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE
                                )
    image = models.ImageField(upload_to='Banners',width_field="width_field",height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = ('Banner')
        verbose_name_plural = ('Banners')
        ordering = ['id']


class SiteInfo(models.Model):
    """ Common SiteInfo."""

    name = models.CharField(max_length=70)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE
                                )
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = ('Site info')
        verbose_name_plural = ('Site info')
        ordering = ['id']


class Sections(models.Model):
    """ Sections in frontend """

    title = models.CharField(max_length=144)
    content = models.TextField(blank=False)
    description = models.TextField(blank=True)
    css_classes = models.TextField(blank=True)
    sub_category = models.ForeignKey(
                                        SiteSubCategories,
                                        on_delete=models.CASCADE
                                    )
    link = models.CharField(max_length=144)
    image = models.ImageField(upload_to='services/section_img',width_field="width_field",height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:

        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
        ordering = ['id']


class FAQ(models.Model):
    """ Frecuent asked questions """

    question = models.CharField(max_length=144)
    sub_category = models.ForeignKey(
                                    SiteSubCategories,
                                    on_delete=models.CASCADE
                                )
    answers = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:

        verbose_name = ('Frecuent asked cuestion')
        verbose_name_plural = ('Frecuent asked cuestions')
        ordering = ['-sub_category']
