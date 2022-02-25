from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import jwt

from Support_test import settings


class UserManager(BaseUserManager):
    """
    User manager class.
    """

    def create_user(self, first_name, second_name, email, password=None):
        """
        Creates and returns a user.
        """
        if first_name is None:
            raise TypeError('Users must have a first name.')

        if second_name is None:
            raise TypeError('Users must have a second name.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(first_name=first_name, second_name=second_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, second_name, email, password):
        """
        Creates and returns a superuser.
        """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(first_name, second_name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """

    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        User.token is self._generate_jwt_token()
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.first_name + self.last_name

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=3)

        token = jwt.encode({'id': self.pk, 'exp': int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
