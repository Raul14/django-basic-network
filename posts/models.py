from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile

# Create your models here.

class Post(models.Model):
    #Functionality keys:
    author = models.ForeignKey(
                Profile,
                on_delete=models.CASCADE,
                related_name='self_posts',
                null=True
            )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    liked = models.ManyToManyField(
                User,
                default=None,
                blank=True
            )
    
    #Content keys:
    body = models.TextField()
    picture = models.ImageField(
                upload_to='images',
                blank=True
            )

    ##METHODS:

    def __str__(self):
        return str(self.pk) #Research about this primary key inheritance
                            # from models.Model

    #................................................................