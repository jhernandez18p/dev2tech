from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    """# Class to generate Sitemap"""
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        """# Method to return urls"""
        return ['Home', 'about', 'contact', 'done',]

    def location(self, item):
        """# Method to return urls"""
        return reverse(item)
