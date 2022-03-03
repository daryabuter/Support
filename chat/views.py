# from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import ChatBox
from . import serializers


class ChatBoxListView(viewsets.ModelViewSet):
    """Users ChatBox List"""

    serializer_class = serializers.ListChatBoxSerializer

    def get_queryset(self):
        return (
            ChatBox.objects.filter(user_id=self.kwargs.get('pk')).select_related('creator').prefetch_related('chat_box')
        )


class ChatBoxView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ChatBox.objects.all().select_related('creator').prefetch_related('chat_box')
    serializers_class = serializers.ChatBoxSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
