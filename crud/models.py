from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email= models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=254)
    avatar = models.ImageField(upload_to = 'uploads/',default='profile.jpg') 
    playlist = models.TextField(null=True,blank=True,default='your playlist...')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    REQUIRED_FILEDS = []


# C reate/add = POST    
# R etrieve/Fetch = GET
# U pdate/Edit = PUT
# D elete/Remove = DELETE

