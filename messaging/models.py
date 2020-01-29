from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint, Q

User = get_user_model()


class ChatQuerySet(models.QuerySet):
    def find_all_of(self, user):
        return self.filter(Q(initiator=user) | Q(acceptant=user)).all()


class Chat(models.Model):
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_initiated')
    acceptant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_accepted')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['initiator', 'acceptant'], name='chat_unique_constraint'),
        ]

    def get_opposite_user(self, user):
        return self.acceptant if user == self.initiator else self.initiator

    objects = ChatQuerySet.as_manager()


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(max_length=255)
    viewed_at = models.DateTimeField(null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
