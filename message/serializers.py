from rest_framework import serializers

from .models import Message
from users.serializers import ChatUserSerializer

# from chat.serializers import ChatBoxSerializer


class MessageSerializer(serializers.ModelSerializer):
    user = ChatUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"


class ChatMessageSerializer(serializers.ModelSerializer):
    user = ChatUserSerializer()

    class Meta:
        model = Message
        fields = "__all__"
