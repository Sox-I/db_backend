from django.urls import path, include
from dbproject.views.settings.getinfo import InfoView
from dbproject.views.settings.register import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getinfo/', InfoView.as_view(), name="settings_getinfo"),
    path('register/', UserView.as_view(), name="settings_register")
]