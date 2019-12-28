from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    phone_num = models.BigIntegerField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile-pic/', default='default/default.png')

    is_client = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

class Banners_details(models.Model):
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # name = models.CharField(max_length=32, null=True, blank=True)
    price = models.IntegerField()
    location = models.CharField(max_length=32)
    size = models.CharField(max_length=16)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
        