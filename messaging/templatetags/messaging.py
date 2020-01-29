from django.template import Library
from django.urls import reverse
from django.utils.timesince import timesince

register = Library()


@register.simple_tag(takes_context=True)
def receiver_photo(context, chat, *args, **kwargs):
    user = context['request'].user
    opposite_user = chat.acceptant if chat.initiator == user else chat.initiator
    return opposite_user.profile.photo.url


@register.simple_tag(takes_context=True)
def receiver_name(context, chat, *args, **kwargs):
    user = context['request'].user
    opposite_user = chat.acceptant if chat.initiator == user else chat.initiator
    return '%s %s' % (opposite_user.first_name, opposite_user.last_name)


@register.simple_tag(takes_context=True)
def receiver_last_message(context, chat, *args, **kwargs):
    message = chat.messages.order_by('-created_at').first()
    return message.text[:20] + ' ...'


@register.simple_tag(takes_context=True)
def receiver_last_message_time(context, chat, *args, **kwargs):
    message = chat.messages.order_by('-created_at').first()
    return timesince(message.created_at)


@register.simple_tag(takes_context=True)
def receiver_new_messages_count(context, chat, *args, **kwargs):
    user = context['request'].user
    opposite_user = chat.acceptant if chat.initiator == user else chat.initiator
    return chat.messages.filter(viewed_at__isnull=True, from_user=opposite_user).count()


@register.simple_tag(takes_context=True)
def message_direction(context, message, *args, **kwargs):
    user = context['request'].user
    return 'pull-right'if user == message.from_user else 'convo-left'


@register.simple_tag(takes_context=True)
def chat_active(context, chat, *args, **kwargs):
    url = context['request'].path
    return 'active'if url == reverse('chat_detail', args=[chat.id]) else ''
