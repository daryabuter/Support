from __future__ import absolute_import, unicode_literals
from time import sleep
from celery import shared_task
from django.core.mail import send_mail

from Support_test.settings import EMAIL_HOST_USER
from .models import ChatBox


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_tasks(chat_pk):
    """Celery task for sending email"""
    with open('email_templ') as f_input:
        list_data = f_input.read()
        template = list_data.split('\n\n')

    chat = ChatBox.objects.get(pk=chat_pk)
    send_to = chat.creator.email
    user_email = [
        send_to,
    ]
    sleep(3)
    send_mail(template[0], template[1], EMAIL_HOST_USER, user_email, fail_silently=False)

    return None
