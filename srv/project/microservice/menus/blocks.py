from wagtail import blocks
from django.template.loader import render_to_string


# Create your models here.
class MenuItem(blocks.StructBlock):
    template = 'menu/text.html'
    title = blocks.CharBlock()
    href = blocks.CharBlock(default="#")

    def render_basic(self, value, context=None):
        return render_to_string(self.template,context=value)


class MenuPage(MenuItem):
    href = blocks.PageChooserBlock()
    template = 'menu/page.html'


class FooterMenuItem(MenuItem):
    template = 'menu/footer_text.html'


class FooterMenuPage(MenuPage):
    href = blocks.PageChooserBlock()
    template = 'menu/footer_page.html'