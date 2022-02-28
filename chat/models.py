from django.db import models
from users.models import User


class ChatBox(models.Model):
    """Chat room model"""

    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.CASCADE)
    supporter = models.ManyToManyField(User, verbose_name="Supporters", related_name="supporter_user")
    date = models.DateTimeField("Create date", auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Status')
    is_frozen = models.BooleanField(default=False, verbose_name='Is frozen')

    class Meta:
        verbose_name = "Chat"


class Message(models.Model):
    """Message model"""

    box = models.ForeignKey(ChatBox, verbose_name="Chat box", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Create date", auto_now_add=True)

    class Meta:
        verbose_name = "Message"
