from django.contrib import admin
from .models import UserProfile, leaderboard
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(leaderboard)