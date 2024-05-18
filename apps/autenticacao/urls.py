from django.urls import path

# from apps.authentication.views import CustomAccessToken, CustomRefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="access_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]