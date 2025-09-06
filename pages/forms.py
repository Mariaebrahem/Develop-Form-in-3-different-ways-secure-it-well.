from django.db import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username",required=True,max_length=200)
    password = forms.CharField(label="password",required=True,max_length=200,widget=forms.PasswordInput)







# 3---------------------------------
# from django import forms
# from .models import login

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = login
#         fields = '__all__'







