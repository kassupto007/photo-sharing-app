from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'password1', 'password2', 'image', 'bio']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'image', 'bio']
