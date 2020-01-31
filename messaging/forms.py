from django.forms import ModelForm

from messaging.models import Message


class MessageSendForm(ModelForm):

    class Meta:
        model = Message
        fields = ('text',)
