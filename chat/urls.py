from rest_framework.routers import DefaultRouter
from . import views

app_name = "chat"
router = DefaultRouter()
router.register("chat", views.ChatBoxView, basename="create")
urlpatterns = router.urls
