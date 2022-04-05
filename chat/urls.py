from rest_framework.routers import DefaultRouter
from . import views

app_name = "chat"
router = DefaultRouter()
router.register('', views.ChatBoxView, basename="chat_box")

urlpatterns = router.urls
