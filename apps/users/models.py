from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    super_user=models.BooleanField(null=False,blank=False,default=False)
    create_hotels=models.BooleanField(null=False,blank=False,default=False)

 
    class Meta:
        ordering = ['user__username']
