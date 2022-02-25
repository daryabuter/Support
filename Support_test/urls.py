from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
