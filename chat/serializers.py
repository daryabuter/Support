from rest_framework import serializers

# from django.contrib.auth.models import User

from chat.models import ChatBox, Message
from users.serializers import UserSerializer


class ChatBoxSerializer(serializers.ModelSerializer):
    """Serializer Chat"""

    creator = UserSerializer()
    supporter = UserSerializer(many=True)

    class Meta:
        model = ChatBox
        fields = ("id", "creator", "supporter", "date")


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ("user", "text", "date")
