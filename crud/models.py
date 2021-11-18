from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email= models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=254)

    REQUIRED_FILEDS = []

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField("image",null = True,blank = True) 
    followers = models.IntegerField()
    following = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


# C reate/add = POST    
# R etrieve/Fetch = GET
# U pdate/Edit = PUT
# D elete/Remove = DELETE

