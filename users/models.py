from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank=True)
    name = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField(max_length = 100, blank = True, null = True)
    username = models.CharField(max_length = 100, null=True, blank=True)
    short_intro = models.CharField(max_length = 200, blank=True, null=True)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, default="profiles/user-default.png",upload_to='profiles/')
    social_github = models.CharField(max_length = 100, null=True, blank=True)
    social_linkedin = models.CharField(max_length = 100, null=True, blank=True)
    social_website = models.CharField(max_length = 100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable = False)
    
    def __str__(self):
        return str(self.user.username)