from django.db import models
from users.models import User


class ChatBox(models.Model):
    """Chat room model"""

    creator = models.ForeignKey(User, verbose_name="Creator", on_delete=models.CASCADE, related_name="creator")
    supporter = models.ManyToManyField(User, verbose_name="Support", related_name="support")
    date = models.DateTimeField("Create date", auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Status')
    is_frozen = models.BooleanField(default=False, verbose_name='Is frozen')

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self):
        return "{} - {}".format(self.creator, self.is_active)
