from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #Functionality keys:
    owner = models.OneToOneField(
                User,
                on_delete=models.CASCADE
            )
    avatar = models.ImageField(
                upload_to='avatars',
                default='avatar.png',
                blank=False
            )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    following = models.ManyToManyField(
                User,
                related_name='self_following',
                blank=True
            )

    #Content keys:
    bio = models.TextField(default="There's no bio so far.")

    ##METHODS:

    def __str__(self):
        return str(self.owner)

    #................................................................