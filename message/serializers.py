from rest_framework import serializers

from .models import Message
from users.serializers import ChatUserSerializer


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message ViewSet"""

    user = ChatUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = "__all__"


class ChatMessageSerializer(serializers.ModelSerializer):
    """Serialization when creating a chat message"""

    user = ChatUserSerializer()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "datetime",
        )
