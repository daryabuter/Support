from rest_framework import permissions
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from .models import ChatBox
from . import serializers
from message.serializers import MessageSerializer
from .tasks import send_email_tasks


class ChatBoxView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    ChatBox ViewSet
    Actions:
    create(), list(), retrieve(), update() - only fot supporters, destroy()
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ChatBoxSerializer
    queryset = ChatBox.objects.all()

    def update(self, request, *args, **kwargs):
        """
        Supporter can change fields:
        is_active(), is_frozen()
        """
        if request.user.is_staff:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data="You dont have permissions", status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        """
        Support sees all chats
        User only those in which he is a member
        """
        queryset = self.queryset
        if self.request.user.is_staff:
            query_set = queryset.all()
        else:
            query_set = queryset.filter(Q(creator=self.request.user) | Q(supporter=self.request.user))
        return query_set

    def get_serializer_class(self):
        actions_to_serializer = {
            "create": serializers.ChatBoxSerializer,
            "list": serializers.ChatBoxListSerializer,
            "retrieve": serializers.ChatBoxDetailSerializer,
            "create_message": MessageSerializer,
            "connect": serializers.ChatBoxSerializer,
            "update": serializers.ChatBoxSupportSerializer,
        }
        return actions_to_serializer.get(self.action, serializers.ChatBoxSerializer)

    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAdminUser])
    def personal_support_chats(self, request):
        """
        Chats in which the supporter is a member
        """
        chats = ChatBox.objects.filter(Q(creator=self.request.user) | Q(supporter=self.request.user))
        serializer = serializers.ChatBoxListSerializer(chats, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAdminUser])
    def active(self, request):
        """
        List of active chats
        """
        chats = ChatBox.objects.filter(is_active=True)
        serializer = serializers.ChatBoxListSerializer(chats, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAdminUser])
    def frozen(self, request):
        """
        List of frozen chats
        """
        chats = ChatBox.objects.filter(is_frozen=True)
        serializer = serializers.ChatBoxListSerializer(chats, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, permission_classes=[permissions.IsAuthenticated])
    def create_message(self, request, *args, **kwargs):
        """
        Create chat messages.
        Only users who are in the chat can create
        """
        chat = self.get_object()
        if request.user == chat.supporter or request.user == chat.creator:
            request.data['chat_box'] = chat.pk
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # celery task activation when a new supporter message appears in the chat
                if request.user.is_staff:
                    send_email_tasks(chat.pk)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="You need connect in the chat", status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True, permission_classes=[permissions.IsAdminUser])
    def connect(self, request, *args, **kwargs):
        """
        Connecting a supporter to a chat
        P.s. The user cannot connect. It connects when creating a chat
        """
        instance = self.get_object()
        chat = ChatBox.objects.get(pk=instance.pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            # connection if there are no supporters in the chat
            if not chat.supporter and request.user.is_staff:
                serializer.save(supporter=self.request.user)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data='Supporter is already in chat.', status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
