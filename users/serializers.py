from rest_framework import serializers
from django.db import transaction

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'second_name', 'password', 'token']

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


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
