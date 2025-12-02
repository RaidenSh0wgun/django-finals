from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class leaderboard(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Rank: {self.rank}"