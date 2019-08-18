from django.template import Library

from ..core.utils import get_media_structure


register = Library()


@register.inclusion_tag("theater/media_dir.html")
def load_dir(media_dict):
    return {'media': media_dict}


@register.simple_tag
def get_media_dict():
    return get_media_structure()
