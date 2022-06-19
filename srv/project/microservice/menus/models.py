from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail import blocks
from wagtail.admin.panels import StreamFieldPanel
from .blocks import MenuItem,MenuPage,FooterMenuPage,FooterMenuItem
from  wagtail.fields import StreamField

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
    trip_advisor = models.URLField(
        help_text='Your Trip Advisor page URL')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')

@register_setting
class GlobalMenu(BaseSetting):
    site_name = models.CharField(default='Netro.fun', max_length=120)
    munus = StreamField([
        ('Page',MenuPage()),
        ('Item',MenuItem())],
    )
    footer = StreamField([
        ('Page',FooterMenuPage()),
        ('Item',FooterMenuItem())],
    )