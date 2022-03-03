from django.contrib import admin
from django.urls import include, path


# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register("admin", admin.site.urls, basename="admin"),
# router.register("users", include('users.urls', namespace='users'), basename="users"),
#
# urlpatterns = []
#
# urlpatterns += router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('chats/', include('chat.urls', namespace='chat')),
]
