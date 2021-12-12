from django.urls import path

from authentication.views import ProfileView, RegisterView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name="api-profile"),
    path('register/', RegisterView.as_view(), name="api-register"),
]