# from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# from django.contrib.auth.models import User
from .models import ChatBox
from .serializers import ChatBoxSerializer


class ChatBoxAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        chat_box = ChatBox.objects.filter(Q(creator=request.user))
        serializer = ChatBoxSerializer(chat_box, many=True)
        return Response({"data": serializer.data})
