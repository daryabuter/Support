from rest_framework import serializers

from users.serializers import ChatUserSerializer
from .models import ChatBox
from message.serializers import ChatMessageSerializer


class ChatBoxSerializer(serializers.ModelSerializer):
    """
    Serialization is about creation. Creator fills in automatically
    """

    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ChatBox
        fields = "__all__"
        read_only_fields = ("supporter", "is_active", "is_frozen", "date")


class ChatBoxListSerializer(serializers.ModelSerializer):
    """
    Serialization for list action.
    """

    creator = ChatUserSerializer()
    supporter = ChatUserSerializer()

    class Meta:
        model = ChatBox
        fields = ("id", "creator", "supporter", "is_active", "is_frozen")


class ChatBoxDetailSerializer(serializers.ModelSerializer):
    """
    Detail serialization.
    """

    creator = ChatUserSerializer()
    supporter = ChatUserSerializer()
    messages = ChatMessageSerializer(read_only=True, many=True)

    class Meta:
        model = ChatBox
        fields = ("id", "creator", "supporter", "is_active", "is_frozen", "date", "messages")


class ChatBoxSupportSerializer(serializers.ModelSerializer):
    """
    Serialization for update() action
    """

    class Meta:
        model = ChatBox
        fields = ("id", "is_active", "is_frozen")
        read_only_fields = ("id",)
