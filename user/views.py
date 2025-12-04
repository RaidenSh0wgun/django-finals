from rest_framework import generics, permissions
from .models import UserProfile, leaderboard
from .serializer import UserProfileSerializer, LeaderboardSerializer
# Create your views here.

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeaderboardView(generics.ListAPIView):
    queryset = leaderboard.objects.all().order_by('-points')
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.AllowAny]