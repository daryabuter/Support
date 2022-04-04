from rest_framework.routers import DefaultRouter
from . import views

app_name = "users"
router = DefaultRouter()
router.register("register", views.RegistrationViewSet, basename="register")
router.register("login", views.LoginViewSet, basename="login")
router.register("user", views.UserApiView, basename="user")
urlpatterns = router.urls
