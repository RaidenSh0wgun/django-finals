from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    
class UserSettings(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='settings')
    receive_newsletter = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    language_preference = models.CharField(max_length=50, default='en')

    def __str__(self):
        return f"{self.user.username}'s settings"