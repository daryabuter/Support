from django.contrib import admin
from .models import ChatBox


class ChatBoxAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "date", "is_active", "is_frozen")
    list_filter = ("is_active", "is_frozen")


admin.site.register(ChatBox, ChatBoxAdmin)
