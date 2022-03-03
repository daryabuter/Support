from rest_framework import serializers


from .models import ChatBox
from message.serializers import ListMessageSerializer


class ChatBoxSerializer(serializers.ModelSerializer):
    source = 'first_name' + 'second_name'
    creator = serializers.ReadOnlyField(source=source)
    supporter = serializers.ReadOnlyField(source=source)
    messages = ListMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatBox
        fields = ("id", "creator", "supporter", "messages", "datetime", "is_active", "is_frozen")


class ListChatBoxSerializer(serializers.ModelSerializer):
    source = 'first_name' + 'second_name'
    creator = serializers.ReadOnlyField(source=source)

    class Meta:
        model = ChatBox
        fields = ("id", "creator", "datetime", "is_active", "is_frozen")
