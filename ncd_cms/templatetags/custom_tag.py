from django import template
from faq.models import FaqCategory

register = template.Library()


@register.simple_tag(name='tag_categories')
def category_list():
    return FaqCategory.objects.all()
