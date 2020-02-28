from django.template import Library
from django.urls import reverse

register = Library()


@register.simple_tag(takes_context=True)
def nav_select(context, view_name, *args, **kwargs):
    url = reverse(view_name)
    request = context['request']
    if url == request.path:
        return 'mint-green'
    else:
        return 'dark-black'


@register.simple_tag(takes_context=True)
def get_request_query(context, query_name, *args, **kwargs):
    return context['request'].GET.get(query_name)
