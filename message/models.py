from django.db import models

from users.models import User
from chat.models import ChatBox


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    chat_box = models.ForeignKey(ChatBox, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=500, blank=True)
    datetime = models.DateTimeField("Create date", auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
