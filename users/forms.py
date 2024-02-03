from dataclasses import field
from email.mime import image

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


# Форма авторизации пользователей
class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'autofocus':True,
                                      'class':'form-control',
                                      'placeholder': 'Введите ваше имя пользователя',
                                      }))
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
                                      'class':'form-control',
                                      'placeholder': 'Введите ваш пароль',})
    )
    class Meta():
        model = User 
        

# Форма регистрации пользователей
class UserRegistrationForm(UserCreationForm):
    class Meta():
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField()   
    last_name = forms.CharField()  
    username = forms.CharField()  
    email = forms.CharField()  
    password1 = forms.CharField()  
    password2 = forms.CharField()  


# Форма редактирвоания профиля
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields =(
            "image",
            "first_name",
            "last_name",
            "username",
            "email",          
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    