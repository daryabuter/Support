from .serializers import RegistrationSerializer
from .renderers import UserJSONRenderer

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class RegistrationViewSet(viewsets.ViewSet):
    """Allow access to endpoint"""

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def create(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def create(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
