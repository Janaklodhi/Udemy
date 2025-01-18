from django.urls import path
from .views import LoginAPIView, VerifyTokenAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('verify-token/', VerifyTokenAPIView.as_view(), name='verify_token'),
]
