from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):  # Измените на forms.Form
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        error_messages={'required': 'Это поле обязательно для заполнения.'}
    )
    email = forms.EmailField(
        label='Электронная почта',
        error_messages={'required': 'Это поле обязательно для заполнения.'}
    )
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("Это поле обязательно для заполнения.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Это имя пользователя уже занято.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Это поле обязательно для заполнения.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже зарегистрирован.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Пароли не совпадают.")

        return cleaned_data
    
class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')