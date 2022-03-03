from rest_framework import serializers

from .models import Message
from users.serializers import UserSerializer


class CreateMessageSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Message
        fields = ("chat_box", "user", "text")


class ListMessageSerializer(serializers.ModelSerializer):
    source = 'user.first_name' + 'user.last_name'
    text = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source=source)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        model = Message
        fields = ("chat_box", "user", "text", "datetime")
