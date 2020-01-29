from django.contrib import admin

from messaging.models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)
