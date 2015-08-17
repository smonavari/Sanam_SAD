__author__ = 'smonavari'

from django import forms
from Sanam.models import *
from django.contrib.auth.models import User



class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        label = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'پست الکترونیک',
            'password': 'رمز عبور',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['gender', 'phoneNumber', 'photo']
        label = {
            'gender': 'جنسیت',
            'phoneNumber': 'تلفن',
            'photo': 'عکس',
        }

