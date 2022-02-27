from django.contrib.auth import authenticate
from rest_framework import serializers
from django.db import transaction

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializing user registration"""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "token"]

        @transaction.atomic()
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("User was not found.")

        return {"email": user.email, "first_name": user.first_name, "last_name": user.last_name, "token": user.token}


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'second_name', 'password', 'token']

    @transaction.atomic()
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
