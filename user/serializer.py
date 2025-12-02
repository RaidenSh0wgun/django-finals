from .models import User, UserProfile, leaderboard
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = leaderboard
        fields = '__all__'