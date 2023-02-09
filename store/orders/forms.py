from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']
        labels = {
            "first_name": "Ваше имя:",
            "last_name": "Ваша фамилия",
            "email": "Ваш email ",
            "city": "Город",
            "address": "Ваш адрес",
            "postal_code": "Индекс",
        }
