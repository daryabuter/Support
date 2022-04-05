from .models import ChatBox


def get_user_mail(chat_pk):
    chat = ChatBox.objects.get(pk=chat_pk)
    return chat.creator.email
