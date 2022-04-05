from rest_framework import permissions
from django.db.models import Q
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from .models import Message
from . import serializers


class MessageViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """
    CRUD Message model
    P.s. Update(): Users can only change the text of the message
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(Q(user=self.request.user))
        return query_set
