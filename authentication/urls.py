from django.urls import path

from authentication.views import ProfileView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('profile/', ProfileView.as_view(), name="api-profile"),
    path('register/', RegisterView.as_view(), name="api-register"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]