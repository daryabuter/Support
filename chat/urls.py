from rest_framework.routers import DefaultRouter
from . import views

app_name = "chat"
router = DefaultRouter()
router.register("create_box", views.ChatBoxAPI, basename="create_box")
urlpatterns = router.urls
