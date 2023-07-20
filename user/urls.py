from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserRegisterView, UserView

urlpatterns = [
    path('user-data/<pk>/', UserView.as_view()),
    path('register/' , UserRegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/' , TokenRefreshView.as_view()),
]