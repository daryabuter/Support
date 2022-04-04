from rest_framework.routers import DefaultRouter
from . import views

app_name = "message"
router = DefaultRouter()
router.register("", views.MessageViewSet, basename="message")
urlpatterns = router.urls
