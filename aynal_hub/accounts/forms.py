from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=100, required=True)
    district = forms.CharField(max_length=100, required=True)
    upazila = forms.CharField(max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = [ 'full_name', 'country', 'district', 'upazila']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name']