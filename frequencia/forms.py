from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class DoRegister(forms.Form):
    now = timezone.now()