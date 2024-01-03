# forms.py
# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from turtle import textinput
from pyexpat import model
from dataclasses import fields

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name','email', 'password1', 'password2']
        
# class RegistrationForm(UserCreationForm):
#     full_name = forms.CharField(max_length=255, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'full_name', 'password1', 'password2']
