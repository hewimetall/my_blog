from wagtail.core.blocks import StreamBlock
from wagtail.core.blocks import CharBlock, StructBlock, BooleanBlock, URLBlock, StreamBlock,ListBlock, \
    RichTextBlock 
from wagtail.images.blocks import ImageChooserBlock

class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class BodyBlock(StreamBlock):
    paragraph = RichTextBlock()
    image_text = ImageText()
    image_carousel = ListBlock(ImageChooserBlock())
    thumbnail_gallery = ListBlock(ImageChooserBlock())
