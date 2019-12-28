from django.contrib import admin
from . models import Banners_details
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(get_user_model())
admin.site.register(Banners_details)