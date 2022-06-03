from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.blocks import StructBlock,CharBlock
# Create your models here.

class Media(StructBlock):
    name = CharBlock(help_text="Названия")
    url = CharBlock(help_text="Ссылка")

    class Media:
        form_classname = "struct-block"
        template = '/block/media.html'

@register_setting(icon='mail')
class SocialMedia(BaseSetting):
    body = StreamField([
        ("", Media()),
    ], verbose_name='Медиа', blank=True)

    panels = [
        StreamFieldPanel('body')
    ]


    telegram = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    habr = models.CharField(max_length=255)

    class Meta:
        verbose = "Социальные настройки"
