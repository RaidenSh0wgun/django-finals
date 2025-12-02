from rest_framework import generics, permissions, serializers
from .serializer import UserProfileSerializer, UserSettingSerializer, UserSerializer
from .models import UserProfile, UserSetting
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

class UserProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class UserSettingListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSettings.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserSettingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSettingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSettings.objects.filter(user=self.request.user)
