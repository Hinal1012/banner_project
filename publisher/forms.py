from django import forms
from .models import Banners_details, User
from django.contrib.auth import get_user_model

class BannerDetailsForm(forms.ModelForm):
    class Meta():
        model = Banners_details
        fields = ('price', 'location', 'size', 'pic')

class UserDetailsForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('profile_pic', 'first_name', 'email', 'phone_num', 'address')