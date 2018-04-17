# -*- coding: utf-8
from django import template

from ..webpack import get_manifest_file_and_type


register = template.Library()


@register.inclusion_tag('easywebpack/webpack_include.html')
def webpack_include(filename):
    return get_manifest_file_and_type(filename)
