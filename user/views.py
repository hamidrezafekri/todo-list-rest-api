from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import Profile
from user.permissions import IsOwnerProfilePermission
from user.serializers import UserCreateSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserView(RetrieveUpdateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsOwnerProfilePermission ,]
    queryset = Profile.objects.all()


