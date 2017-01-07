from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #Class to allow adding additional user fields
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    

    def __str__(self):
        return self.user.username