from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "chat_box")
    list_filter = ("user",)


admin.site.register(Message, MessageAdmin)
