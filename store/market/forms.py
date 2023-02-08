from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reviews, Basket, Feedback, CustomUser
from captcha.fields import CaptchaField

from .models import Favorites


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        CHOICES = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )
        model = Reviews
        fields = ("text", "mark",)
        widget = {
            "text": forms.TextInput,
            "mark": forms.ChoiceField(choices=CHOICES)
        }
        labels = {
            "text": "Ваш отзыв:",
            "mark": "Ваша оценка товару"
        }


class AddBasket(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ("product", "count", "price",)


class UserCreateForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Пароли не совпадют! Попробуйте еще раз!',
    }
    username = forms.CharField(
        label="Ваше ник",
        strip=False,
    )
    first_name = forms.CharField(
        label="Ваше имя",
        strip=False,
    )
    last_name = forms.CharField(
        label="Ваша фамилия",
        strip=False,
    )
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Пароль повторно",
        strip=False,
        help_text="Введите пароль еще раз",
    )
    email = forms.EmailField(
        label="Ваш адрес электронной почты",
    )
    city = forms.CharField(
        label="Укажите город",
    )
    adress = forms.CharField(
        label="Адрес для доставки",
    )
    captcha = CaptchaField(
        label="Введите знаки с картинки"
    )

    class Meta:
        model = User
        fields = ("username", "last_name", "email", 'captcha', 'city',)
        widgets = {"username": forms.TextInput,
                   "last_name": forms.TextInput,
                   "password1": forms.PasswordInput(
                       attrs={'autocomplete': 'new-password'}
                   ),
                   "password2": forms.PasswordInput(
                       attrs={'autocomplete': 'new-password'}
                   ),
                   "email": forms.EmailInput(),
                   "city": forms.TextInput,
                   }


class UserCityForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("user_for_city",)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('email_sender', 'topic', 'text_message',)
        widgets = {"email_sender": forms.EmailInput(),
                   "topic": forms.TextInput,
                   "text_message": forms.TextInput,
                   }


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class AddToFavoritesForm(forms.ModelForm):
    class Meta:
        model = Favorites
        fields = ('product_favorite', 'user',)
