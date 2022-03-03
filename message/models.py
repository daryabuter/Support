from django.db import models

from users.models import User
from chat.models import ChatBox


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    text = models.CharField(max_length=500, blank=True)
    chat_box = models.ForeignKey(ChatBox, related_name="chat_box", on_delete=models.CASCADE)
    datetime = models.DateTimeField("Create date", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.text)
