from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('chats/', include('chat.urls', namespace='chat')),
    path('messages/', include('message.urls', namespace='message')),
]
