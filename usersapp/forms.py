# usersapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ])
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 
                  'phone', 'profile_photo', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 
                  'bio', 'profile_photo']